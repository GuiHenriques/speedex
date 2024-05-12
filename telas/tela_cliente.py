from telas.telaAbstrata import TelaAbstrata
from utils.valildadores import campo_vazio_validador
from utils.valildadores import cpf_validador

import PySimpleGUI as sg

# constantes
SIZE_TEXT = (10, 1)
SIZE_INPUT_TEXT = (30, 1)

class TelaCliente(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento is None:
            return 0
        
        return evento

    def pega_dados_de_cadastro(self):
        layout = [
            [sg.Text("Cadastrar cliente", font=("Arial", 24), justification="center")],
            [sg.Text("Nome:", size=SIZE_TEXT), sg.InputText("", key="nome", size=SIZE_INPUT_TEXT)],
            [sg.Text("CPF:", size=SIZE_TEXT), sg.InputText("", key="cpf", size=SIZE_INPUT_TEXT)],
            [sg.Text("CEP", size=SIZE_TEXT), sg.InputText("", key="cep", size=SIZE_INPUT_TEXT)],
            [sg.Text("Estado", size=SIZE_TEXT), sg.InputText("", key="estado", size=SIZE_INPUT_TEXT)],
            [sg.Text("Cidade", size=SIZE_TEXT), sg.InputText("", key="cidade", size=SIZE_INPUT_TEXT)],
            [sg.Text("Bairro", size=SIZE_TEXT), sg.InputText("", key="bairro", size=SIZE_INPUT_TEXT)],
            [sg.Text("Rua", size=SIZE_TEXT), sg.InputText("", key="rua", size=SIZE_INPUT_TEXT)],
            [sg.Text("Número", size=SIZE_TEXT), sg.InputText("", key="numero", size=SIZE_INPUT_TEXT)],
            [sg.Button("Cadastrar", size=(8, 1))]
        ]

        self.janela = sg.Window("Cadastro", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()


        if evento == "Cadastrar":
            if not self.__campos_sao_validos(valores):
                return evento, None
    
            return evento, valores
        
        return evento, None
    
    def pega_cpf_cliente(self):
        layout = [
            [sg.Text("Digite o CPF:", size=SIZE_TEXT), sg.InputText("", key="cpf", size=SIZE_INPUT_TEXT)],
            [sg.Button("Confirmar", size=(8, 1))]
        ]

        self.janela = sg.Window("Buscar CPF", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Confirmar":
            if not self.__campos_sao_validos(valores):
                return evento, None
            return evento, valores
        
        return evento, None

    def tela_principal(self):
        layout = self.layout_button([
                    "Cadastrar cliente",
                    "Alterar dados de cliente",
                    "Excluir cliente",
                    "Listar clientes"
                ]
        )

        self.janela = sg.Window("Menu de Clientes", layout, element_justification="c")

    def __campos_sao_validos(self, valores):
        if campo_vazio_validador(valores):
            self.mensagem("Por favor, preencha todos os campos.")
            return False

        if not cpf_validador(valores["cpf"]):
            self.mensagem("CPF inválido!")
            return False

        return True