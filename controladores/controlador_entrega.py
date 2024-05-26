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

    def cadastrar_entrega(self):
        dados = self.dados_entrega()
        # funcionario = self.dados_funcionario_entrega()

        # self.registrar_encomenda(valores["conteudo"], valores["peso"], valores_caixa)

        # destino

        # distancia

        # valor total

        # registrar encomenda
        # self.registrar_encomenda(dados)

        # registrar entrega

        # tela entrega cadastrada
        # self.tela.tela_cadastrada()

    def dados_entrega(self):
        while True:
            # Encomenda
            tipos_de_entrega = self.__controlador_sistema.controlador_tipo_de_entrega.nome_tipos_de_entrega()
            evento, valores = self.tela.tela_encomenda(tipos_de_entrega)

            if evento == None or evento == "voltar":
                return

            if valores == None:
                continue

            # cpf do remetente e destinatário existem
            # if not self.__controlador_sistema.controlador_cliente.cpf_existe(valores["cpf_remetente"]):
            #     self.tela.mensagem("CPF do remetente não encontrado")
            #     continue

            # if not self.__controlador_sistema.controlador_cliente.cpf_existe(valores["cpf_destinatario"]):
            #     self.tela.mensagem("CPF do destinatário não encontrado")
            #     continue

            # validação tipo de entrega
            if valores["opcao_entrega"] not in tipos_de_entrega:
                self.tela.mensagem("Tipo de entrega inválido")
                continue

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

            tipo_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.gerar_tipo_de_caixa_cliente(valores_caixa)

        else:
            tipos_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.tipos_de_caixa()
            valores_caixa = self.tela.tela_nao_possui_caixa(tipos_de_caixa)
            
            if valores_caixa == None:
                return False
            
            id_caixa_escolhida = next(key for key, value in valores_caixa.items() if value)
            
            tipo_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.pegar_tipo_de_caixa_por_id(id_caixa_escolhida)

            
        # print("Tipo de Caixa", tipo_de_caixa.nome, tipo_de_caixa.taxa)
        return tipo_de_caixa
