from abc import ABC

import PySimpleGUI as sg


class TelaAbstrata(ABC):
    def __init__(self):
        self.__janela = None

    @property
    def janela(self):
        return self.__janela

    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    def layout_button(self, elementos):
        layout = [
            [sg.Button(elemento, size=(23, 1), pad=(10), key=key + 1)]
            for key, elemento in enumerate(elementos)
        ]
        layout.append(
            [
                sg.Button(
                    "Sair",
                    size=(20, 1),
                    pad=(10),
                    key=0,
                    button_color=("white", "#FF403F"),
                )
            ]
        )
        return layout

    def mensagem(self, mensagem: str):
        sg.Popup(f"{mensagem:40}")

    def abrir_janela(self):
        evento, valores = self.__janela.Read()
        return evento, valores

    def fechar_janela(self):
        self.__janela.Close()
