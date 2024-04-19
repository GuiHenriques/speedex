import tkinter as tk

class TelaSistema:
    def __init__(self):
        self.__window = None

    def abre_tela(self):
        self.tela_principal()

    def tela_principal(self):
        self.__window = tk.Tk()
        radio1 = tk.Radiobutton(self.__window, text="Tipo de entrega")
        radio1.pack()
        radio2 = tk.Radiobutton(self.__window, text="Tipo de caixa")
        radio2.pack()
        botao = tk.Button(self.__window, text="Ok")
        botao.pack()
        self.__window.mainloop()