import PySimpleGUI as sg

class TelaTiposDeEntrega:
    def __init__(self, ControladorTiposDeEntrega):
        self.__janela = None
        self.__controlador_tipo_de_entrega = ControladorTiposDeEntrega

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        self.fechar_janela()

        if evento == "Cadastro de tipos de entrega":
            return valores
            
        return None


    def tela_principal(self):
        layout = [
            [sg.Text("Nome: "), sg.InputText("", key="nome")],
            [sg.Text("Taxa: "), sg.InputText("", key="taxa")],
            [sg.Text("Descrição: "), sg.InputText("", key="descricao")],
            [sg.Push(), sg.Button("Cadastrar"), sg.Push()]
        ]

        self.__janela = sg.Window("Cadastro de tipos de entrega", layout)

    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def abrir_janela(self):
        evento, valores = self.__janela.Read()
        return evento, valores

    def fechar_janela(self):
        self.__janela.Close()