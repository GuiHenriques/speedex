import PySimpleGUI as sg

class TelaLogin:
    def __init__(self, ControladorLogin):
        self.__janela = None
        self.__controlador_login = ControladorLogin

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Login":
            return valores
            
        return None


    def tela_principal(self):
        layout = [
            [sg.Text("Email: "), sg.InputText("", key="email")],
            [sg.Text("Senha: "), sg.InputText("", key="senha")],
            [sg.Push(), sg.Button("Login"), sg.Push()]
        ]

        self.__janela = sg.Window("Login", layout)

    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def abrir_janela(self):
        evento, valores = self.__janela.Read()
        return evento, valores

    def fechar_janela(self):
        self.__janela.Close()