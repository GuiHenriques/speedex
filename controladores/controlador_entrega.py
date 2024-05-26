from telas.tela_entrega import TelaEntrega
from utils.valildadores import algum_campo_e_vazio, campo_numerico_validador
from entidades.repositorios.entrega_repositorio import EntregaRepositorio
from entidades.modelos.destinatario import Destinatario
from entidades.modelos.encomenda import Encomenda


class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela = (
            TelaEntrega() if not controlador_sistema.development_mode else None
        )
        self.__repositorio = EntregaRepositorio(controlador_sistema)
        self.__controlador_sistema = controlador_sistema

    @property
    def tela(self):
        return self.__tela

    def cadastrar_entrega(self):
        dados = self.dados_entrega()
        # {
        #     "cpf_remetente": "15645692845",
        #     "cpf_destinatario": "54766065808",
        #     "descricao": "bola",
        #     "peso": "12",
        #     "opcao_entrega": ("aaa",),
        #     "possui_caixa": False,
        #     "tipo_de_caixa": "<entidades.modelos.tipo_de_caixa.TipoDeCaixa object at 0x000002D56F2A5610>",
        # }

        remetente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(
            dados["cpf_remetente"]
        )
        print("Remetente", remetente)

        destinatario = (
            self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(
                dados["cpf_destinatario"]
            )
        )
        print("Destinatario", destinatario)

        encomenda = Encomenda(dados["descricao"], dados["peso"], dados["tipo_de_caixa"])
        print("Encomenda", encomenda)
        # self.cadastrar_encomenda(encomenda)

        tipo_de_entrega = self.__controlador_sistema.controlador_tipo_de_entrega.pegar_tipo_de_entrega_por_nome(
            dados["opcao_entrega"][0]
        )
        print("Tipo de entrega", tipo_de_entrega)

        # funcionario = self.dados_funcionario_entrega()

        # destino
        cep_destino = destinatario.cep

        # distancia
        # api google maps

        # valor total
        # formula

        # registrar encomenda
        # self.registrar_encomenda(dados)

        # registrar entrega

        # tela entrega cadastrada
        # self.tela.tela_cadastrada()

    def dados_entrega(self):
        while True:
            # Encomenda
            tipos_de_entrega = (
                self.__controlador_sistema.controlador_tipo_de_entrega.nome_tipos_de_entrega()
            )
            evento, valores = self.tela.tela_encomenda(tipos_de_entrega)

            if evento == None or evento == "voltar":
                return

            if valores == None:
                continue

            # validação de cpfs e tipo de entrega
            # if not self.__cpfs_e_tipo_de_entrega_valido(valores["cpf_remetente"],valores["cpf_destinatario"],valores["opcao_entrega"],tipos_de_entrega,):
            #     continue

            # dados da caixa
            tipo_de_caixa = self.dados_tipo_caixa(valores["possui_caixa"])
            if not tipo_de_caixa:
                continue

            valores["tipo_de_caixa"] = tipo_de_caixa

            return valores

    def dados_tipo_caixa(self, possui_caixa):

        if possui_caixa:
            valores_caixa = self.tela.tela_possui_caixa()
            # valores_caixa = {"altura": "10", "largura": "10", "comprimento": "10"}

            if valores_caixa == None:
                return False

            tipo_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.gerar_tipo_de_caixa_cliente(
                valores_caixa
            )

        else:  # Caixa SPEEDEX
            tipos_de_caixa = (
                self.__controlador_sistema.controlador_tipo_de_caixa.tipos_de_caixa()
            )
            valores_caixa = self.tela.tela_nao_possui_caixa(tipos_de_caixa)

            if valores_caixa == None:
                return False

            id_caixa_escolhida = next(
                key for key, value in valores_caixa.items() if value
            )

            tipo_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.pegar_tipo_de_caixa_por_id(
                id_caixa_escolhida
            )

        print("Tipo de Caixa", tipo_de_caixa)
        return tipo_de_caixa

    def cadastrar_encomenda(self, encomenda):
        cadastrado, msg_error = self.__repositorio.registrar_encomenda(encomenda)
        if cadastrado:
            self.tela.mensagem("Encomenda cadastrada com sucesso")
            return True
        else:
            self.tela.mensagem(f"Não foi possível cadastrar a encomenda:\n{msg_error}")
            return False

    def __cpfs_e_tipo_de_entrega_valido(
        self, cpf_remetente, cpf_destinatario, tipo_de_entrega, tipos_de_entrega
    ):
        # cpf do remetente existe
        if not self.__controlador_sistema.controlador_cliente.cpf_existe(cpf_remetente):
            self.tela.mensagem("CPF do remetente não encontrado")
            return False

        if not self.__controlador_sistema.controlador_cliente.cpf_existe(
            cpf_destinatario
        ):
            self.tela.mensagem("CPF do destinatário não encontrado")
            return False

        # destinatario é instância de destinatario
        if not isinstance(
            self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(
                cpf_destinatario
            ),
            Destinatario,
        ):
            self.tela.mensagem("Destinatário não tem endereço cadastrado")
            return False

        # validação tipo de entrega
        if tipo_de_entrega not in tipos_de_entrega:
            self.tela.mensagem("Tipo de entrega inválido")
            return False

        return True
