from telas.tela import Tela

import PySimpleGUI as sg


class TelaFuncionario(Tela):
    def __init__(self):
        super().__init__()

    def tela_login(self):
        layout = [
            [sg.Text("Login", font=("Arial", 24), justification="center")],
            [sg.Text("Email:", size=(5, 1)), sg.InputText("", key="email", size=(30, 1))],
            [sg.Text("Senha:", size=(5, 1)), sg.InputText("", key="senha", password_char="*", size=(30, 1))],
            [sg.Button("Login", size=(8, 1))],
            [sg.Text("Ainda não possui uma conta?", size=(30, 1), font=("Arial", 10), justification="center", pad=((0, 0), (10, 0)))],
            [sg.Text("Clique aqui para se cadastrar", text_color="blue", font=("Arial", 10, "underline"), enable_events=True, key="cadastro")],
        ]


        self.janela = sg.Window("Login", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Login": # Se o funcionário quiser voltar para a tela de login
            return evento, valores

        elif evento == "cadastro": # Quando o usuário clicar em cadastrar
            return evento, valores

        return evento, None

    def tela_cadastro(self):
        layout = [
            [sg.Text("Cadastro", font=("Helvetica", 18), justification="center")],
            [sg.Text("CPF", size=(6, 1)), sg.InputText("", key="cpf", size=(30, 1))],
            [sg.Text("Nome", size=(6, 1)), sg.InputText("", key="nome", size=(30, 1))],
            [sg.Text("Email", size=(6, 1)), sg.InputText("", key="email", size=(30, 1))],
            [sg.Text("Senha", size=(6, 1)), sg.InputText("", key="senha", password_char="*", size=(30, 1))],
            [sg.Button("Cadastrar", size=(8, 1))],
            [sg.Text("Já possui uma conta?", size=(30, 1), justification="center", pad=((0, 0), (10, 0)))],
            [sg.Text("Clique aqui para fazer login", text_color="blue", font=("Arial", 11, "underline"), enable_events=True, key="login")],
        ]


        self.janela = sg.Window("Cadastro", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Cadastrar":
            return evento, valores
        
        elif evento == "login":
            return evento, valores

        return evento, None
