from telas.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela: TelaRelatorio = TelaRelatorio()

    def abre_tela(self):
        lista_opcoes = {
            1: self.relatorio_de_encomendas,
            2: self.relatorio_de_tipos_de_caixa,
            3: self.relatorio_de_tipos_de_entrega,
        }

        while True:
            opcao = self.__tela.abre_tela()
            if opcao == 0:
                return

            opcao_escolhida = lista_opcoes[opcao]
            opcao_escolhida()

    def relatorio_de_encomendas(self): ...
    def relatorio_de_tipos_de_caixa(self): ...

    def relatorio_de_tipos_de_entrega(self):
        self.__tela.pega_periodo()
