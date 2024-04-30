import PySimpleGUI as sg
from telas.tela import Tela


class TelaEncomenda(Tela):
    def __init__(self):
        super().__init__()

    def tela_encomenda(self):
        layout = [
            [sg.Text("Encomenda", font=("Arial", 24), justification="center")],
            [
                sg.Text("CPF do Remetente:", size=(15, 1)),
                sg.InputText("", key="cpf_cliente", size=(30, 1)),
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
                sg.Text(
                    "Opção de entrega:",
                    size=(15, 1),
                    justification="center",
                ),
                sg.Combo(
                    ["Expressa", "Normal", "Econômica"],
                    key="opcao_entrega",
                    size=(28, 1),
                ),
            ],
            [
                sg.Text("Possui caixa?", size=(15, 1)),
                sg.Radio("Sim", "caixa", key="caixa_sim", default=True),
                sg.Radio("Não", "caixa", key="caixa_nao"),
            ],
            [sg.Button("Proximo", size=(8, 1))],
            [
                sg.Text(
                    "Voltar",
                    text_color="blue",
                    font=("Arial", 10, "underline"),
                    enable_events=True,
                    key="voltar",
                )
            ],
        ]

        self.janela = sg.Window("Encomenda", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Proximo":
            # {
            #     "cpf_cliente": "15645692845",
            #     "cpf_destinatario": "54766065808",
            #     "descricao": "Bola",
            #     "opcao_entrega": "Expressa",
            #     "caixa_sim": True,
            #     "caixa_nao": False,
            # }
            return valores

        else:
            return None

    def tela_possui_caixa(self):
        layout = [
            [sg.Text("Caixa", font=("Arial", 24), justification="center")],
            [
                sg.Text("Altura:", size=(15, 1)),
                sg.InputText("", key="altura", size=(30, 1)),
            ],
            [
                sg.Text("Largura:", size=(15, 1)),
                sg.InputText("", key="largura", size=(30, 1)),
            ],
            [
                sg.Text("Comprimento:", size=(15, 1)),
                sg.InputText("", key="comprimento", size=(30, 1)),
            ],
            [sg.Button("Proximo", size=(8, 1))],
        ]

        self.janela = sg.Window("Caixa", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Proximo":
            return valores

        return None

    def tela_nao_possui_caixa(self):
        layout = [
            [sg.Text("Caixa", font=("Arial", 24), justification="center")],
            [
                sg.Text(
                    "Selecione uma opção de caixa:",
                    size=(30, 1),
                    justification="center",
                )
            ],
            # loop para cada caixa
            [
                sg.Radio("Pequena", "tamanho_caixa", key="pequena", size=(8, 1)),
                sg.Text(f"{10}x{10}x{10} - R$ {10}"),
            ],
            [
                sg.Radio("Média", "tamanho_caixa", key="media", size=(8, 1), default=True),
                sg.Text(f"{20}x{20}x{20} - R$ {20}"),
            ],
            [
                sg.Radio("Grande", "tamanho_caixa", key="grande", size=(8, 1)),
                sg.Text(f"{30}x{30}x{30} - R$ {30}"),
            ],
            [sg.Button("Proximo", size=(8, 1))],
        ]

        self.janela = sg.Window("Caixa", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()
        

        if evento == "Proximo":
            return valores

        return None

    # defina um bom nome para a tela de encomenda cadastrada com sucesso
    def tela_cadastrada(self):
        layout = [
            [
                sg.Text(
                    "Encomenda cadastrada com sucesso!",
                    font=("Arial", 24),
                    justification="center",
                )
            ],
            [sg.Button("Voltar", size=(8, 1))],
        ]

        self.janela = sg.Window("Encomenda", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Voltar":
            return None

        return None
