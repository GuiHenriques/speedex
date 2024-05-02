from telas.tela import Tela

import PySimpleGUI as sg


class TelaCliente(Tela):
    def __init__(self):
        super().__init__()

    def tela_cadastro(self):
        layout = [
            [sg.Text("Login", font=("Arial", 24), justification="center")],
            [sg.Text("Nome:", size=(5, 1)), sg.InputText("", key="nome", size=(30, 1))],
            [sg.Text("CPF:", size=(5, 1)), sg.InputText("", key="cpf", size=(30, 1))]
            [sg.Text("Endereço:")],
            [sg.Text("CEP", size=(5, 1)), sg.InputText("", key="cep", size=(30, 1))]
            [sg.Text("Rua", size=(5, 1)), sg.InputText("", key="rua", size=(30, 1))]
            [sg.Text("Número", size=(5, 1)), sg.InputText("", key="numero", size=(30, 1))]
            [sg.Text("Bairro", size=(5, 1)), sg.InputText("", key="bairro", size=(30, 1))]
            [sg.Text("Cidade", size=(5, 1)), sg.InputText("", key="cidade", size=(30, 1))]
            [sg.Text("Estado", size=(5, 1)), sg.InputText("", key="Estado", size=(30, 1))]
            [sg.Button("Cadastrar", size=(8, 1))]
        ]

        self.janela = sg.Window("Cadastro", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Cadastrar":
            return evento, valores
        
        return evento, None