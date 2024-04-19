from telas.tela_sistema import TelaSistema
from controladores.controlador_login import ControladorLogin

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema();
        self.__controlador_login = ControladorLogin()

    def inicializa_sistema(self):
        self.login()
        self.abre_tela()

    def abre_tela():
        ...

    def login(self):
        self.__controlador_login.abre_tela()

    def tela_principal(self):
        lista_opcoes = {
            1: self.login
        }

        while True:
            opcao = self.__tela_sistema.abre_tela()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()