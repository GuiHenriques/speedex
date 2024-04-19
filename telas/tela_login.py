import tkinter as tk

class TelaLogin:
    def __init__(self, ControladorLogin):
        self.__window = tk.Tk()
        self.__controlador_login = ControladorLogin

    def abre_tela(self):
        self.tela_principal()

    def tela_principal(self):
        self.__window.title("Login")
        email = tk.Entry(self.__window)
        email.pack()
        senha = tk.Entry(self.__window)
        senha.pack()
        botao = tk.Button(self.__window, text="Login",
                          command=lambda: self.retornar_dados(email.get(), senha.get()))
        botao.pack()
        self.__window.mainloop()

    def retornar_dados(self, email, senha):
        login_concedido = self.__controlador_login.verificar_entrada(email, senha)
        if login_concedido:
            self.__window.destroy()
            return