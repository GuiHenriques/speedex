import tkinter as tk

class TelaLogin:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Login")

    def abre_tela(self):
        self.tela_principal()

    def tela_principal(self):
        self.__window.title("Login")
        email = tk.Entry(self.__window)
        email.pack()
        senha = tk.Entry(self.__window)
        senha.pack()
        botao = tk.Button(self.__window, text="Login",
                          command=lambda: self.login(email.get(), senha.get()))
        botao.pack()
        self.__window.mainloop()

    def login(self, email, senha):
        self.__window.destroy()
        label1 = tk.Label(text=email)
        label1.pack()
        label2 = tk.Label(text=senha)
        label2.pack()
        self.__window.mainloop()