import PySimpleGUI as sg

class TelaCadastro:
    def __init__(self, ControladorCadastro):
        self.__janela = None
        self.__controlador_cadastro = ControladorCadastro

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Cadastrar":
            return valores
            
        return None

    def tela_principal(self):
        layout = [
            [sg.Text("Nome: "), sg.InputText("", key="nome")],
            [sg.Text("CPF: "), sg.InputText("", key="cpf")],
            [sg.Text("Email: "), sg.InputText("", key="email")],
            [sg.Text("Senha: "), sg.InputText("", key="senha")],
            [sg.Push(), sg.Button("Cadastrar"), sg.Push()]
        ]

        self.__janela = sg.Window("Cadastro", layout)

    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def abrir_janela(self):
        evento, valores = self.__janela.Read()
        return evento, valores

    def fechar_janela(self):
        self.__janela.Close()