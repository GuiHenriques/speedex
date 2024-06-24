import PySimpleGUI as sg
from telas.telaAbstrata import TelaAbstrata

from utils.valildadores import data_validador, cpf_validador

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

    def pega_dados_relatorio_entrega(self):
        layout = [
            [sg.Radio("Cliente", "tipo_relatorio", key="cliente", default=True)],
            [sg.Text("CPF: "), sg.Input(key="cpf", size=(20, 1))],
            [sg.Radio("Período (dd/mm/aaaa)", "tipo_relatorio", key="periodo")],
            [
                sg.Text("De: "),
                sg.Input(key="data_inicio", size=(12, 1)),
                sg.Text("Até: "),
                sg.Input(key="data_fim", size=(12, 1)),
            ],
            [sg.Button("Confirmar")],
        ]

        self.janela = sg.Window("Relatório de Entrega", layout)

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Confirmar":

            if valores["cliente"]:
                if cpf_validador(valores["cpf"]):
                    return evento, valores
                else:
                    self.mensagem("CPF inválido")
                    return "CPF inválido", None

            elif valores["periodo"]:
                if data_validador(valores["data_inicio"]) and data_validador(valores["data_fim"]):
                    return evento, valores
                else:
                    self.mensagem("Data inválida")
                    return "Data inválida", None
