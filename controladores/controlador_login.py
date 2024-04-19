from telas.tela_login import TelaLogin


class ControladorLogin:
    def __init__(self):
        self.__tela_login = TelaLogin(self)

    def verificar_entrada(self, email, senha):
        if email == "login" and senha == "senha":
            return True
        else:
            return False


    def abre_tela(self):
        while True:
            self.__tela_login.abre_tela()
        