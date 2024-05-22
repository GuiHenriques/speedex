from telas.telaAbstrata import TelaAbstrata
from utils.valildadores import algum_campo_e_vazio

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

    def pega_dados_de_cliente(self, nome: str = "", cep: str = "",
                              estado: str = "", cidade: str = "", bairro: str = "",
                              rua: str = "", numero: str = ""):
        
        layout = [
            [sg.Text("Cadastrar cliente" if nome == "" else "Atualizar cliente", font=("Arial", 24), justification="center")],
            [sg.Text("CPF:", size=SIZE_TEXT), sg.InputText("", key="cpf", size=SIZE_INPUT_TEXT)] if nome == "" else [],
            [sg.Text("Nome:", size=SIZE_TEXT), sg.InputText(nome, key="nome", size=SIZE_INPUT_TEXT)],
            [sg.Text("CEP", size=SIZE_TEXT), sg.InputText(cep, key="cep", size=SIZE_INPUT_TEXT)],
            [sg.Text("Estado", size=SIZE_TEXT), sg.InputText(estado, key="estado", size=SIZE_INPUT_TEXT)],
            [sg.Text("Cidade", size=SIZE_TEXT), sg.InputText(cidade, key="cidade", size=SIZE_INPUT_TEXT)],
            [sg.Text("Bairro", size=SIZE_TEXT), sg.InputText(bairro, key="bairro", size=SIZE_INPUT_TEXT)],
            [sg.Text("Rua", size=SIZE_TEXT), sg.InputText(rua, key="rua", size=SIZE_INPUT_TEXT)],
            [sg.Text("Número", size=SIZE_TEXT), sg.InputText(numero, key="numero", size=SIZE_INPUT_TEXT)],
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
            if algum_campo_e_vazio(valores):
                self.mensagem("Digite o CPF!")
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
        if "cpf" in valores:
            if valores["cpf"] == "":
                self.mensagem("CPF pode ser vazio!")
                return False
        
        if valores["nome"] == "":
            self.mensagem("Nome não pode ser vazio!")
            return False

        if valores["cep"] == "":
            if valores["estado"] != "" or valores["cidade"] != "" or valores["bairro"] != "" or valores["rua"] != "" or valores["numero"] != "":
                self.mensagem("CEP não pode ser vazio!")
                return False
        else:
            if valores["estado"] == "" or valores["cidade"] == "" or valores["bairro"] == "" or valores["rua"] == "" or valores["numero"] == "":
                self.mensagem("Digite também os outros campos de endereço!")
                return False

        return True