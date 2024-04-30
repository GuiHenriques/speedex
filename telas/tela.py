from abc import ABC

import PySimpleGUI as sg


class Tela(ABC):
    def __init__(self):
        self.__janela = None

    @property
    def janela(self):
        return self.__janela
    
    @janela.setter
    def janela(self, janela):
        self.__janela = janela

    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def abrir_janela(self):
        evento, valores = self.__janela.Read()
        return evento, valores
    
    def fechar_janela(self):
        self.__janela.Close()