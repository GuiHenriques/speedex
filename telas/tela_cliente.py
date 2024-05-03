from telas.tela import Tela

import PySimpleGUI as sg

# constantes
SIZE_TEXT = (5, 1)
SIZE_INPUT_TEXT = (30, 1)

class TelaCliente(Tela):
    def __init__(self):
        super().__init__()

    def abre_tela(self):
        evento, valores = self.tela_principal()
        self.fechar_janela()

        if evento in (None, "Cancelar") or valores["0"]:
            return 0
        elif valores["1"]:
            return 1
        elif valores["2"]:
            return 2
        elif valores["3"]:
            return 3
        elif valores["4"]:
            return 4

    def tela_cadastro(self):
        layout = [
            [sg.Text("Cadastrar cliente", font=("Arial", 24), justification="center")],
            [sg.Text("Nome:", size=SIZE_TEXT), sg.InputText("", key="nome", size=SIZE_INPUT_TEXT)],
            [sg.Text("CPF:", size=SIZE_TEXT), sg.InputText("", key="cpf", size=SIZE_INPUT_TEXT)],
            [sg.Text("Endereço:", size=SIZE_TEXT), sg.InputText("", key="endereco", size=SIZE_INPUT_TEXT)],
            [sg.Text("CEP", size=SIZE_TEXT), sg.InputText("", key="cep", size=SIZE_INPUT_TEXT)],
            [sg.Text("Rua", size=SIZE_TEXT), sg.InputText("", key="rua", size=SIZE_INPUT_TEXT)],
            [sg.Text("Número", size=SIZE_TEXT), sg.InputText("", key="numero", size=SIZE_INPUT_TEXT)],
            [sg.Text("Bairro", size=SIZE_TEXT), sg.InputText("", key="bairro", size=SIZE_INPUT_TEXT)],
            [sg.Text("Cidade", size=SIZE_TEXT), sg.InputText("", key="cidade", size=SIZE_INPUT_TEXT)],
            [sg.Text("Estado", size=SIZE_TEXT), sg.InputText("", key="Estado", size=SIZE_INPUT_TEXT)],
            [sg.Button("Cadastrar", size=(8, 1))]
        ]

        self.janela = sg.Window("Cadastro", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Cadastrar":
            return evento, valores
        
        return evento, None
    
    def tela_principal(self):
        layout = [
            [sg.Radio("Cadastrar cliente.", 'Radio1', key='1')],
            [sg.Radio("Alterar dados de cliente.", "Radio1", key="2")],
            [sg.Radio("Excluir cliente.", "Radio1", key="3")],
            [sg.Radio("Listar clientes.", "Radio1", key="4")],
            [sg.Radio("Retornar para o menu principal.", "Radio1", default=True, key="0")],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]

        self.janela = sg.Window("Menu de Clientes", layout, element_justification="c")

        evento, valores = self.abrir_janela()

        if evento == "Confirmar":
            return evento, valores
        
        return evento, None