from controladores import controlador_sistema
from telas.tela_relatorio import TelaRelatorio
from entidades.repositorios.relatorio_repositorio import RelatorioRepositorio
from utils.conversores import str_para_datetime


class ControladorRelatorio:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema: "controlador_sistema.ControladorSistema" = (
            controlador_sistema
        )
        self.__tela: TelaRelatorio = TelaRelatorio()
        self.__repositorio = RelatorioRepositorio(controlador_sistema)

    @property
    def tela(self) -> TelaRelatorio:
        return self.__tela

    def abre_tela(self):
        lista_opcoes = {
            1: self.relatorio_de_entrega,
            2: self.relatorio_de_tipos_de_caixa,
            3: self.relatorio_de_tipos_de_entrega,
        }

        while True:
            opcao = self.__tela.abre_tela()
            if opcao == 0:
                return

            opcao_escolhida = lista_opcoes[opcao]
            opcao_escolhida()

    def relatorio_de_entrega(self):
        while True:
            evento, valores = self.__tela.pega_dados_relatorio_entrega()

            if evento is None or valores is None:
                return

            # Verifica se o CPF do remetente existe
            if valores["cliente"]:
                cpf = valores["cpf"]

                if not self.__controlador_sistema.controlador_cliente.cpf_existe(cpf):
                    self.tela.mensagem("CPF não encontrado")
                    continue

                entregas = self.__repositorio.pega_entregas_por_cpf(cpf)

            else:
                inicio = str_para_datetime(valores["data_inicio"])
                fim = str_para_datetime(valores["data_fim"])

                entregas = self.__repositorio.pega_entrega_por_periodo(inicio, fim)

            self.tela.relatorio_de_entregas(entregas)

    def relatorio_de_tipos_de_caixa(self): ...

    def relatorio_de_tipos_de_entrega(self):
        while True:
            evento, valores = self.__tela.pega_periodo()

            if evento is None or valores is None:
                return

            inicio = str_para_datetime(valores["data_inicio"])
            fim = str_para_datetime(valores["data_fim"])
            
            tipos_de_entrega = self.__repositorio.relatorio_tipo_de_entrega(inicio, fim)
            
            self.tela.relatorio_de_tipo_de_entrega(tipos_de_entrega)