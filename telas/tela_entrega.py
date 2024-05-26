import PySimpleGUI as sg
from telas.telaAbstrata import TelaAbstrata

from utils.valildadores import (
    algum_campo_e_vazio,
    campo_numerico_validador,
    cpf_validador,
)


class TelaEntrega(TelaAbstrata):
    def __init__(self):
        super().__init__()

    def tela_encomenda(self, tipos_de_entrega: list):
        layout = [
            [sg.Text("Encomenda", font=("Arial", 24), justification="center")],
            [
                sg.Text("CPF do Remetente:", size=(15, 1)),
                sg.InputText("", key="cpf_remetente", size=(30, 1)),
            ],
            [
                sg.Text("CPF do Destinatário:", size=(15, 1)),
                sg.InputText("", key="cpf_destinatario", size=(30, 1)),
            ],
            [
                sg.Text("Conteúdo:", size=(15, 1)),
                sg.InputText("", key="descricao", size=(30, 1)),
            ],
            [
                sg.Text("Peso (kg):", size=(15, 1)),
                sg.InputText("", key="peso", size=(30, 1)),
            ],
            [
                sg.Text(
                    "Opção de entrega:",
                    size=(15, 1),
                    justification="center",
                ),
                sg.Combo(tipos_de_entrega, key="opcao_entrega", size=(28, 1)),
            ],
            [
                sg.Checkbox("Encomenda possui caixa?", key="possui_caixa"),
            ],
            [sg.Button("Proximo", size=(8, 1))],
            [
                sg.Text(
                    "Voltar",
                    text_color="blue",
                    font=("Arial", 10, "underline"),
                    enable_events=True,
                    key="voltar",
                ),
            ],
        ]

        self.janela = sg.Window("Encomenda", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        # {
        #     "cpf_remetente": "123.456.789-00",
        #     "cpf_destinatario": "987.654.321-00",
        #     "conteudo": "Bola",
        #     "peso": "10",
        #     "opcao_entrega": "Expressa",
        #     "possui_caixa": True,
        # }

        if evento == "Proximo":
            if self.__campos_sao_validos_encomenda(valores):
                return evento, valores

            return evento, None

        return evento, None

    def tela_possui_caixa(self):
        layout = [
            [sg.Text("Caixa", font=("Arial", 24), justification="center")],
            [sg.Text("Digite as dimensões da caixa (cm):", size=(30, 1))],
            [
                sg.Text("Altura:", size=(10, 1)),
                sg.InputText("", key="altura", size=(30, 1)),
            ],
            [
                sg.Text("Largura:", size=(10, 1)),
                sg.InputText("", key="largura", size=(30, 1)),
            ],
            [
                sg.Text("Comprimento:", size=(10, 1)),
                sg.InputText("", key="comprimento", size=(30, 1)),
            ],
            [sg.Button("Proximo", size=(8, 1))],
        ]

        self.janela = sg.Window("Caixa", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()
        # valores = {"altura": "10", "largura": "10", "comprimento": "10"}
        if evento == "Proximo":
            if self.__campos_sao_validos_possui_caixa(valores):
                return valores
            
            self.mensagem("As dimensões da caixa devem ser números inteiros positivos.")

        return None

    def tela_nao_possui_caixa(self, tipos_de_caixa: list):
        radio_layout = []

        layout = [
            [sg.Text("Caixa", font=("Arial", 24), justification="center")],
            [
                sg.Text(
                    "Selecione uma opção de caixa:",
                    size=(30, 1),
                    justification="center",
                )
            ],
        ]
        # loop para cada caixa
        # [
        #     sg.Radio("Pequena", "tamanho_caixa", key="pequena", size=(8, 1)),
        #     sg.Text(f"{10}x{10}x{10} - R$ {10}"),
        # ],

        for caixa in tipos_de_caixa:
            layout.append(
                [
                    sg.Radio(caixa[1], "tamanho_caixa", key=caixa[0], size=(8, 1)),
                    sg.Text(f"{caixa[3]} x {caixa[4]} x {caixa[5]}"),
                    sg.Text(f"R$ {caixa[2]}"),
                ]
            )

        layout.append([sg.Button("Proximo", size=(8, 1))])

        self.janela = sg.Window("Caixa", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        print(valores)
        self.fechar_janela()

        if evento == "Proximo":
            # pegar dimensões da caixa selecionada e retornar
            # valores = {"altura": "10", "largura": "10", "comprimento": "10"}
            return valores

        return None

    def tela_entrega_cadastrada(self):
        layout = [
            [
                sg.Text(
                    "Encomenda cadastrada com sucesso!",
                    font=("Arial", 18),
                    justification="center",
                )
            ],
            [sg.Text("Valor total: R$ 30,00")],
            [sg.Text("Origem: São Paulo")],
            [sg.Text("Destino: Rio de Janeiro")],
            [sg.Button("OK", size=(8, 1), button_color=("white", "green"))],
        ]

        self.janela = sg.Window("Encomenda", layout, element_justification="c")

        self.abrir_janela()
        self.fechar_janela()

        return None

    def __campos_sao_validos_encomenda(self, valores):

        # verificar se todos os campos foram preenchidos
        if algum_campo_e_vazio(valores):
            self.mensagem("Por favor, preencha todos os campos.")
            return False

        # verificar se o cpf do remetente e do destinatario existem no banco de dados
        if not cpf_validador(valores["cpf_remetente"]):
            self.mensagem("CPF do remetente inválido.")
            return False

        if not cpf_validador(valores["cpf_destinatario"]):
            self.mensagem("CPF do destinatário inválido.")
            return False

        # verificar se o cpf do remetente e do destinatario são iguais
        if valores["cpf_remetente"] == valores["cpf_destinatario"]:
            self.mensagem("CPF do remetente e do destinatário são iguais.")
            return False

        # verificar se o peso é um número
        if not valores["peso"].isnumeric():
            self.mensagem("O peso deve ser um número inteiro positivo.")
            return False

        return True

    def __campos_sao_validos_possui_caixa(self, valores_caixa):

        # verificar se todos os campos foram preenchidos
        if algum_campo_e_vazio(valores_caixa):
            self.mensagem("Por favor, preencha todos os campos.")
            return False

        # verificar se a altura, largura e comprimento são números
        if not campo_numerico_validador(valores_caixa):
            self.mensagem("As dimensões da caixa devem ser números inteiros positivos.")
            return False

        return True
