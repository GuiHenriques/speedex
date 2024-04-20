from telas.tela_login import TelaLogin


class ControladorLogin:
    def __init__(self):
        self.__tela_login = TelaLogin(self)

    def abre_tela(self):
        while True:
            valores = self.__tela_login.abre_tela()
            if valores == None:
                return False

            if self.verificar_entrada(valores["email"], valores["senha"]):
                return True
            else:
                self.__tela_login.mensagem("Login ou senha incorreto.")
    
    def verificar_entrada(self, email, senha):
        if email == "login" and senha == "senha":
            return True
        else:
            return False