from telas.tela_cliente import TelaCliente
from entidades.repositorios.cliente_repositorio import ClienteRepositorio
from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario
from entidades.modelos.endereco import Endereco

from utils.valildadores import cpf_validador
from utils.valildadores import campo_vazio_validador


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__tela = TelaCliente() if not controlador_sistema.development_mode else None
        self.__controlador_sistema = controlador_sistema
        self.__repositorio = ClienteRepositorio(controlador_sistema)

    def abre_tela(self):
        lista_opcoes = {
            1: self.menu_cadastro_de_cliente,
            0: "Retornar para o menu principal",
        }

        while True:
            opcao = self.__tela.abre_tela()
            if opcao == 0:
                return

            opcao_escolhida = lista_opcoes[opcao]
            opcao_escolhida()

    def menu_cadastro_de_cliente(self):
        evento, valores = self.__tela.pega_dados_de_cadastro()
        
        if valores == None:
            return
        
        if not self.__verificar_campos_validos(valores):
            return

        cpf = valores["cpf"]
        nome = valores["nome"]
        endereco = Endereco(
            valores["cep"],
            valores["estado"],
            valores["cidade"],
            valores["bairro"],
            valores["rua"],
            valores["numero"],
        )

        self.cadastrar_cliente(cpf, nome, endereco)

    def cadastrar_cliente(self, cpf: str, nome: str, endereco: Endereco = None) -> bool:
        if not cpf_validador(cpf):
            self.__mensagem("CPF inválido!")
            return False

        cliente = None
        if endereco is None:
            cliente = Remetente(cpf, nome)
        else:
            cliente = Destinatario(cpf, nome, endereco)
        
        if self.__verificar_se_cpf_existe(cliente.cpf):
            self.__mensagem("CPF já cadastrado!")
            return False

        cliente_foi_cadastrado, msg_error = self.__repositorio.registrar_cliente(cliente)
        if cliente_foi_cadastrado:
            self.__mensagem("Cliente cadastrado!")
            return cliente
        else:
            self.__mensagem(f"Não foi possível cadastrar o cliente!\n{msg_error}")
            return False
        
    def excluir_cliente(self, cpf: str):
        if not cpf_validador(cpf):
            self.__mensagem("CPF inválido!")
            return False

        cliente = self.__repositorio.pega_cliente(cpf)
        cliente_foi_excluido, msg_error = self.__repositorio.excluir_cliente(cliente)
        if cliente_foi_excluido:
            return cliente
        else:
            self.__mensagem(f"Não foi possível excluir o cliente!\n{msg_error}")
            return False


    def __verificar_se_cpf_existe(self, cpf: str):
        if self.__repositorio.pega_cliente(cpf) == None:
            return False
        else:
            return True
        
    def __verificar_campos_validos(self, valores):
        if campo_vazio_validador(valores):
            self.__mensagem("Por favor, preencha todos os campos.")
            return False

        if not cpf_validador(valores["cpf"]):
            self.__mensagem("CPF inválido!")
            return False

        return True

    def __mensagem(self, msg):
        try:
            self.__tela.mensagem(msg)
        except AttributeError:
            pass