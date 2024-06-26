from entidades.modelos.entrega import Entrega
from telas.tela_entrega import TelaEntrega
from utils.apis import get_distancia
from utils.frete import calcula_valor_total
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
    def tela(self) -> TelaEntrega | None:
        if self.__tela is not None:
            return self.__tela

    def dados_entrega(self):
        # Verifica se há tipos de entrega cadastrados
        if not self.__controlador_sistema.controlador_tipo_de_entrega.tipos_de_entrega():
            self.tela.mensagem("Não há tipos de entrega cadastrados")
            return

        # Obtém os dados da encomenda
        dados = self.dados_encomenda()
        if not dados:
            return

        # Recupera o remetente pelo CPF
        remetente = self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(
            dados["cpf_remetente"]
        )

        # Recupera o destinatário pelo CPF
        destinatario = (
            self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(
                dados["cpf_destinatario"]
            )
        )

        # Recupera o funcionário logado
        funcionario = self.__controlador_sistema.session

        # Cria uma nova encomenda
        encomenda = Encomenda(dados["descricao"], dados["peso"], dados["tipo_de_caixa"])
        self.cadastrar_encomenda(encomenda)

        # Define o ID da encomenda
        id = self.__repositorio.pegar_id_ultima_encomenda()
        encomenda.id = id

        tipo_de_caixa = dados["tipo_de_caixa"]

        # Recupera o tipo de entrega
        tipo_de_entrega = self.__controlador_sistema.controlador_tipo_de_entrega.pegar_tipo_de_entrega_por_nome(
            dados["opcao_entrega"][0]
        )

        # Calcula a distância usando uma API
        dados_distancia = get_distancia(
            destinatario.endereco.cep, tipo_de_entrega.velocidade
        )
        distancia = dados_distancia["distance"]["value"]

        # Calcula o valor total do frete
        valor_total = calcula_valor_total(
            distancia,
            encomenda.peso,
            tipo_de_caixa.dimensoes,
            tipo_de_caixa.taxa,
            tipo_de_entrega.taxa,
        )

        # Cria uma nova entrega
        entrega = Entrega(
            remetente,
            destinatario,
            encomenda,
            tipo_de_entrega,
            funcionario,
            distancia,
        )
        self.cadastrar_entrega(entrega)

        # tela de entrega cadastrada
        self.tela.entrega_cadastrada(entrega, valor_total)

    def dados_encomenda(self):
        while True:
            # Obtém os nomes dos tipos de entrega
            nome_dos_tipos_de_entrega = self.__controlador_sistema.controlador_tipo_de_entrega.nome_tipos_de_entrega()
            # Exibe a tela para obter os dados da encomenda
            evento, valores = self.tela.tela_encomenda(nome_dos_tipos_de_entrega)

            if evento is None or evento == "voltar":
                return

            if valores is None:
                continue

            # Valida os CPFs e o tipo de entrega
            if not self.__cpfs_e_tipo_de_entrega_valido(
                valores["cpf_remetente"],
                valores["cpf_destinatario"],
                valores["opcao_entrega"],
                nome_dos_tipos_de_entrega,
            ):
                continue

            # Obtém os dados do tipo de caixa
            tipo_de_caixa = self.dados_tipo_caixa(valores["possui_caixa"])
            if not tipo_de_caixa:
                continue

            valores["tipo_de_caixa"] = tipo_de_caixa

            return valores

    def dados_tipo_caixa(self, possui_caixa):
        if possui_caixa:  # caixa do cliente
            valores_caixa = self.tela.tela_possui_caixa()

            if valores_caixa is None:
                return False

            # Gera o tipo de caixa do cliente
            tipo_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.gerar_tipo_de_caixa_cliente(
                valores_caixa
            )

        else:  # caixa da SPEEDEX
            # Verifica se há tipos de caixa
            if not self.__controlador_sistema.controlador_tipo_de_caixa.tipos_de_caixa():
                self.tela.mensagem("Não há tipos de caixa cadastrados")
                return False

            tipos_de_caixa = (
                self.__controlador_sistema.controlador_tipo_de_caixa.tipos_de_caixa()
            )
            valores_caixa = self.tela.tela_nao_possui_caixa(tipos_de_caixa)

            if valores_caixa is None:
                return False

            # Identifica a caixa escolhida pelo cliente
            id_caixa_escolhida = next(
                key for key, value in valores_caixa.items() if value
            )

            # Recupera o tipo de caixa pelo ID
            tipo_de_caixa = self.__controlador_sistema.controlador_tipo_de_caixa.pegar_tipo_de_caixa_por_id(
                id_caixa_escolhida
            )

        return tipo_de_caixa

    def cadastrar_encomenda(self, encomenda):
        # Registra a encomenda no repositório
        cadastrado, msg_error = self.__repositorio.registrar_encomenda(encomenda)

        if not cadastrado:
            self.tela.mensagem(f"Não foi possível cadastrar a encomenda:\n{msg_error}")
            return False
        else:
            return True

    def cadastrar_entrega(self, entrega):
        # Registra a entrega no repositório
        cadastrado, msg_error = self.__repositorio.registrar_entrega(entrega)

        if cadastrado:
            self.tela.mensagem("Entrega cadastrada com sucesso")
            return True
        else:
            self.tela.mensagem(f"Não foi possível cadastrar a entrega:\n{msg_error}")
            return False

    def __cpfs_e_tipo_de_entrega_valido(
        self, cpf_remetente, cpf_destinatario, tipo_de_entrega, tipos_de_entrega
    ):
        # Verifica se o CPF do remetente existe
        if not self.__controlador_sistema.controlador_cliente.cpf_existe(cpf_remetente):
            self.tela.mensagem("CPF do remetente não encontrado")
            return False

        # Verifica se o CPF do destinatário existe
        if not self.__controlador_sistema.controlador_cliente.cpf_existe(
            cpf_destinatario
        ):
            self.tela.mensagem("CPF do destinatário não encontrado")
            return False

        # Verifica se o destinatário tem um endereço cadastrado
        if not isinstance(
            self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(
                cpf_destinatario
            ),
            Destinatario,
        ):
            self.tela.mensagem("Destinatário não tem endereço cadastrado")
            return False

        # Verifica se o tipo de entrega é válido
        if tipo_de_entrega not in tipos_de_entrega:
            self.tela.mensagem("Tipo de entrega inválido")
            return False

        return True

    def relatorio_de_tipos_de_entrega_mais_utilizados(self, inicio, fim):
        todos_tipos_de_entrega = (
            self.__repositorio.tipos_de_entrega_mais_utilizados_por_periodo(inicio, fim)
        )

        return todos_tipos_de_entrega
