from telas.tela_login import TelaLogin


class ControladorLogin:
    def __init__(self):
        self.__tela_login = TelaLogin()

    def abre_tela(self):
        opcao = self.__tela_login.abre_tela()