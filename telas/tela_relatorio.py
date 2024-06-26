import PySimpleGUI as sg
from telas.telaAbstrata import TelaAbstrata

from utils.valildadores import data_validador, cpf_validador

BUTTON_SIZE = (8, 1)


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
            [sg.Text("Período (dd/mm/aaaa)")],
            [
                sg.Text("De: "),
                sg.Input(key="data_inicio", size=(12, 1)),
                sg.Text("Até: "),
                sg.Input(key="data_fim", size=(12, 1)),
            ],
            [sg.Button("Confirmar")],
        ]

        self.janela = sg.Window("Selecionar período", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Confirmar":
            if not self.__validar_periodo(valores["data_inicio"], valores["data_fim"]):
                self.mensagem("Data inválida!")
                return evento, None

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
                if self.__validar_periodo(valores["data_inicio"], valores["data_fim"]):
                    return evento, valores
                else:
                    self.mensagem("Data inválida")
                    return "Data inválida", None
        else:
            return None, None

    def relatorio_de_entregas(self, entregas):
        if entregas is None or len(entregas) == 0:
            self.mensagem("Nenhuma entrega encontrada.")
            return
        
        header = (
            "ID",
            "CPF Remet.",
            "Remetente",
            "CPF Destinat.",
            "Destinatario",
            "CPF Func.",
            "Funcionario",
            "Altura",
            "Largura",
            "Comprim.",
            "Tipo de Cx",
            "Conteudo",
            "Taxa Cx",
            "Tipo Entrega",
            "Taxa E.",
            "CEP",
            "Data",
            "Distancia",
            "Valor"
        )

        layout = [
            [sg.Table(entregas, header)],
            [sg.Button("Ok", size=BUTTON_SIZE)],
        ]

        self.janela = sg.Window("Relatório de Entregas", layout, element_justification="c")
        self.abrir_janela()
        self.fechar_janela()

    def relatorio_de_tipo_de_entrega(self, dados_tipo_de_entrega):
        if dados_tipo_de_entrega is None or len(dados_tipo_de_entrega) == 0:
            self.mensagem("Nenhum tipo de entrega utilizado neste período.")
            return

        header = ["ID", "Nome", "Taxa", "Quantidade de usos"]
        layout = [
            [sg.Table(dados_tipo_de_entrega, header)],
            [sg.Button("Ok", size=BUTTON_SIZE)],
        ]

        self.janela = sg.Window("Relatório de Tipos de Entrega", layout, element_justification="c")

        self.abrir_janela()
        self.fechar_janela()
        return True

    def __validar_periodo(self, inicio, fim):
        if data_validador(inicio) and data_validador(fim):
            return True
        else:
            return False
