from telas.tela_entrega import TelaEntrega
from utils.valildadores import algum_campo_e_vazio, campo_numerico_validador
from entidades.repositorios.encomenda_repositorio import EncomendaRepositorio

# from entidades.repositorios.cliente_repositorio import ClienteRepositorio


class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela = (TelaEntrega() if not controlador_sistema.development_mode else None)
        self.__repositorio = EncomendaRepositorio(controlador_sistema)
        self.__controlador_sistema = controlador_sistema

    @property
    def tela(self):
        return self.__tela

    def abre_tela(self):
        while True:
            evento, valores_encomenda = self.tela.tela_encomenda()

            if evento == None or evento == "voltar":
                return

            if valores_encomenda == None:
                continue

            # cpf do remetente e destinatário existem
            if not self.__controlador_sistema.controlador_cliente.cpf_existe(valores_encomenda["cpf_remetente"]):
                self.tela.mensagem("CPF do remetente não encontrado")
                continue

            if not self.__controlador_sistema.controlador_cliente.cpf_existe(valores_encomenda["cpf_destinatario"]):
                self.tela.mensagem("CPF do destinatário não encontrado")
                continue

            # se usuario tem caixa
            if valores_encomenda["possui_caixa"]:
                valores_caixa = self.tela.tela_possui_caixa()
                # valores_caixa = {"altura": "10", "largura": "10", "comprimento": "10"}
                if valores_caixa == None:
                    return False

                # validação dos campos
                if not self.__campos_sao_validos_caixa(valores_caixa):
                    continue

            else:
                valores_caixa = self.tela.tela_nao_possui_caixa()
                # pegar dimensões da caixa selecionada

                if valores_caixa == None:
                    return False

            # registrar encomenda
            valores = {**valores_encomenda, **valores_caixa}
            print(valores)
            self.processar_encomenda(valores)
            break

    def registrar_encomenda(self, valores):

        # registrar encomenda no banco de dados
        # self.__repositorio.registrar_encomenda()

        self.tela.tela_cadastrada()

    def valida_encomenda(self, valores):
        # cpf

        # tipo de entrega
        pass