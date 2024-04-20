import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()

    def tela_principal(self):
        layout = [
            [sg.Radio("Tipo de Entrega", "Radio1", key="1")],
            [sg.Radio("Fechar", "Radio1", default=True, key="0")],
            [sg.Push(), sg.Button("Confirmar")],
        ]

        self.__window = sg.Window("Menu Principal", layout)

    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def abrir_janela(self):
        evento, valores = self.__window.Read()
        return evento, valores
    
    def fechar_janela(self):
        self.__window.Close()
