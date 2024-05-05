from telas.tela import Tela
import PySimpleGUI as sg


class TelaEntrega(Tela):
    def __init__(self):
        super().__init__()

    def tela_entrega(self):
        layout = [
            [sg.Text("Entrega", font=("Arial", 24), justification="center")],
            [
                sg.Text("CPF do Remetente:", size=(15, 1)),
                sg.InputText("", key="cpf_remetente", size=(30, 1)),
            ],
            [
                sg.Text("CPF do Destinatário:", size=(15, 1)),
                sg.InputText("", key="cpf_destinatario", size=(30, 1)),
            ],
            [
                sg.Text("ID da Encomenda:", size=(15, 1)),
                sg.InputText("", key="id_encomenda", size=(30, 1)),
            ],
            [
                sg.Text(
                    "Tipo de entrega:",
                    size=(15, 1),
                    justification="center",
                ),
                sg.Combo(
                    ["Expressa", "Normal", "Econômica"],
                    key="tipo_entrega",
                    size=(28, 1),
                ),
            ],
            [sg.Button("Registrar", size=(8, 1))],
        ]

        self.janela = sg.Window("Entrega", layout, element_justification="c")

        evento, valores = self.abrir_janela()
        self.fechar_janela()
        # {
        #     "cpf_remetente": "123.456.789-00",
        #     "cpf_destinatario": "987.654.321-00",
        #     "id_encomenda": "1",
        #     "tipo_entrega": "Expressa",
        # }

        if evento == "Registrar":
            return evento, valores

        return evento, None
