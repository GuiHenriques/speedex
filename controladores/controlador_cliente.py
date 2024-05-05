from telas.tela_cliente import TelaCliente
from entidades.repositorios.cliente_repositorio import ClienteRepositorio
from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario
from entidades.modelos.endereco import Endereco


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__tela = TelaCliente() if not controlador_sistema.development_mode else None
        self.__controlador_sistema = controlador_sistema
        self.__repositorio = ClienteRepositorio(controlador_sistema)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_cliente,
            0: "Retornar para o menu principal",
        }

        while True:
            opcao = self.__tela.abre_tela()
            if opcao == 0:
                return

            opcao_escolhida = lista_opcoes[opcao]
            opcao_escolhida()

    def cadastrar_cliente(self, cpf: str, nome: str, endereco: Endereco) -> bool:
        cliente = None
        if endereco is None:
            cliente = Remetente(cpf, nome)
        else:
            cliente = Destinatario(cpf, nome, endereco)

        cliente_cadastrado, msg_error = self.__repositorio.registrar_cliente(cliente)
        if cliente_cadastrado:
            self.mensagem("Cliente cadastrado!")
            return cliente
        else:
            self.mensagem(f"Não foi possível cadastrar o cliente!\n{msg_error}")
            return False

    def mensagem(self, msg):
        try:
            self.__tela.mensagem(msg)
        except AttributeError:
            pass