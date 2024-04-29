from telas.tela import Tela

import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self):
        super().__init__()

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        if evento is None or valores["0"]:
            opcao_escolhida = 0
        elif valores["1"]:
            opcao_escolhida = 1
        self.fechar_janela()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Tipo de Entrega", "Radio1", key="1")],
            [sg.Radio("Fechar", "Radio1", default=True, key="0")],
            [sg.Push(), sg.Button("Confirmar")],
        ]

        self.janela = sg.Window("Menu Principal", layout)
