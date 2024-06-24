from telas.telaAbstrata import TelaAbstrata

import PySimpleGUI as sg


class TelaRelatorio(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def abre_tela(self):
        self.tela_principal()
        evento, _ = self.abrir_janela()
        self.fechar_janela()

        if evento is None:
            return 0

        return evento

    def tela_principal(self):
        layout = self.layout_button(
            [
                "Relatório de Entregas",
                "Relatório de Tipos de Caixa",
                "Relatório de Tipos de Entrega",
            ]
        )

        self.janela = sg.Window("Menu de Relatórios", layout, element_justification="c")

    def pega_periodo(self):
        layout = [
            [sg.Text("Período")],
            [sg.Input],
            [sg.Button("Confirmar")],
        ]

        self.janela = sg.Window("Selecionar período", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Confirmar":
            return evento, valores

        return evento, None
