from telas.telaAbstrata import TelaAbstrata

import PySimpleGUI as sg


class TelaSistema(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        
        if evento is None:
            return 0

        self.fechar_janela()
        return evento

    def tela_principal(self):
        layout = self.layout_button(
            [
                "Entregas",
                "Clientes",
                "Tipos de Entrega",
                "Tipos de Caixa",
                "Relatórios",
            ]
        )

        self.janela = sg.Window("Menu Principal", layout, element_justification="c")
