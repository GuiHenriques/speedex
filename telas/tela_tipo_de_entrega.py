import PySimpleGUI as sg

class TelaTiposDeEntrega:
    def __init__(self, ControladorTipoDeEntrega):
        self.__janela = None
        self.__controlador_tipo_de_entrega = ControladorTipoDeEntrega

    def abre_tela(self):
        self.tela_principal()
        evento, valores = self.abrir_janela()
        ###
        self.fechar_janela()
        ###

        if evento in (None, "Cancelar") or valores["0"]:
            opcao_escolhida = 0
        elif valores["1"]:
            opcao_escolhida = 1
        elif valores["2"]:
            opcao_escolhida = 2
        elif valores["3"]:
            opcao_escolhida = 3
        elif valores["4"]:
            opcao_escolhida = 4

        self.fechar_janela()
        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Incluir tipo de entrega.", 'Radio1', key='1')],
            [sg.Radio("Alterar tipo de entrega.", "Radio1", key="2")],
            [sg.Radio("Excluir tipo de entrega.", "Radio1", key="3")],
            [sg.Radio("Listar tipos de entrega.", "Radio1", key="4")],
            [
                sg.Radio(
                    "Retornar para o menu principal.", "Radio1", default=True, key="0"
                )
            ],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__janela = sg.Window("Menu de tipos de entrega", layout, finalize=True)

    def pega_dados_tipo_de_entrega(self):
        layout = [
            [sg.Text("Nome: "), sg.InputText("", key="nome")],
            [sg.Text("Taxa: "), sg.InputText("", key="taxa")],
            [sg.Text("Descrição: "), sg.InputText("", key="descricao")],
            [sg.Push(), sg.Button("Cadastrar"), sg.Cancel("Cancelar")]
        ]

        self.__janela = sg.Window("Cadastro de tipos de entrega", layout)
        evento , valores = self.abrir_janela()
        entrada_invalida = False

        if evento in (None, "Cancelar"):
            self.fechar_janela()
            return
        
        # if valores["nome"]==None or valores["taxa"]==None or valores["descricao"]==None:
        #     sg.popup_error("Todos os campos devem ser preenchidos!")
        #     entrada_invalida = True

        self.fechar_janela()
        if entrada_invalida:
            return
        else:
            return {
                "nome": valores["nome"],
                "taxa": valores["taxa"],
                "descricao": valores["descricao"],
            }
        
    def seleciona_codigo_tipo_de_entrega(self):
        layout = [
            [sg.Text("Código: "), sg.InputText("", key="codigo")],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.__janela = sg.Window("Selecionar código de um tipo de entrega", layout)
        evento, valores = self.abrir_janela()

        if evento in (None, "Cancelar"):
            self.fechar_janela()
            return

        try:
            valores["codigo"] = int(valores["codigo"])
        except:
            sg.popup_error("Digite um número inteiro.")
            self.fechar_janela()
            return

        self.fechar_janela()
        return valores["codigo"]
    


    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def abrir_janela(self):
        evento, valores = self.__janela.Read()
        return evento, valores

    def fechar_janela(self):
        self.__janela.Close()