from telas.telaAbstrata import TelaAbstrata

import PySimpleGUI as sg

class TelaTiposDeCaixa(TelaAbstrata):
    def __init__(self, ControladorTipoDeCaixa):
        self.__controlador_tipo_de_caixa = ControladorTipoDeCaixa

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

        return opcao_escolhida

    def tela_principal(self):
        layout = [
            [sg.Radio("Incluir tipo de caixa.", 'Radio1', key='1')],
            [sg.Radio("Alterar tipo de caixa.", "Radio1", key="2")],
            [sg.Radio("Excluir tipo de caixa.", "Radio1", key="3")],
            [sg.Radio("Listar tipos de caixa.", "Radio1", key="4")],
            [
                sg.Radio(
                    "Retornar para o menu principal.", "Radio1", default=True, key="0"
                )
            ],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.janela = sg.Window("Menu de tipos de caixa", layout, finalize=True)

    
    def pega_dados_tipo_de_caixa(self):
        
        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        layout = [
            [sg.Text("Nome: "), sg.InputText("", key="nome")],
            [sg.Text("Taxa: "), sg.InputText("", key="taxa")],
<<<<<<< HEAD
            [sg.Text("Altura em metros: "), sg.InputText("", key="altura")],
            [sg.Text("Largura em metros: "), sg.InputText("", key="largura")],
            [sg.Text("Comprimento em metros: "), sg.InputText("", key="comprimento")],
=======
            [sg.Text("Dimensões: "), sg.InputText("", key="dimensoes")],
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
            [sg.Push(), sg.Button("Cadastrar"), sg.Cancel("Cancelar")]
        ]

        self.janela = sg.Window("Cadastro de tipos de caixa", layout)
        evento , valores = self.abrir_janela()
        entrada_invalida = False

        if evento in (None, "Cancelar"):
            self.fechar_janela()
            return
        


        if not all(valores.values()):
            sg.popup("Você deve preencher todos os campos!")
            self.fechar_janela()
            entrada_invalida = True
            return
        
        if not is_float(valores["taxa"]):
            sg.popup("A taxa deve ser um número válido!")
            self.fechar_janela()
            entrada_invalida = True
            return
<<<<<<< HEAD
        
        if not is_float(valores["altura"]) or not is_float(valores["largura"]) or not is_float(valores["comprimento"]):
            sg.popup("Altura, largura e comprimento devem ser números válidos!")
            self.fechar_janela()
            entrada_invalida = True
            return

        if float(valores["altura"]) > 1 or float(valores["largura"]) > 1 or float(valores["comprimento"]) > 1:
            sg.popup("Altura, largura e comprimento não podem ser maiores que 1m individualmente!")
            self.fechar_janela()
            entrada_invalida = True
            return

        if (float(valores["altura"]) + float(valores["largura"])  + float(valores["comprimento"])) > 2:
            sg.popup("A soma de altura, largura e comprimento não pode exceder 2m!")
            self.fechar_janela()
            entrada_invalida = True
            return
=======

>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb

        self.fechar_janela()
        if entrada_invalida:
            return
        else:
            return {
                "nome": valores["nome"],
                "taxa": float(valores["taxa"]),
<<<<<<< HEAD
                "altura": float(valores["altura"]),
                "largura": float(valores["largura"]),
                "comprimento": float(valores["comprimento"]),

=======
                "dimensoes": valores["dimensoes"],
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
            }
        
    def seleciona_codigo_tipo_de_caixa(self):
        layout = [
            [sg.Text("Código: "), sg.InputText("", key="codigo")],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.janela = sg.Window("Selecionar código de um tipo de caixa", layout)
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
    

    def mostra_tipo_de_caixa(self, resultados):
        string_resultados=""
        if not resultados:
            string_resultados = "Nenhum tipo de caixa cadastrado!"
        else:
            for row in resultados:
<<<<<<< HEAD
                string_resultados += f"Código:{row[0]} \nNome: {row[1]} \nTaxa: {row[2]} \nAltura: {row[4]}m \nLargura: {row[3]}m\nComprimento: {row[5]}m\n\n"
=======
                string_resultados += f"Código:{row[0]} \nNome: {row[1]} \nTaxa: {row[2]} \nDimensões: {row[3]}\n \n"
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb

        width_size = 50
        height_size = 20
        layout = [
            [
                sg.Multiline(
                    string_resultados,
                    size=(width_size, height_size),
                    disabled=True,
                    text_color="#000",
                    background_color="",
                )
            ],
            [sg.Push(), sg.Button("Ok"), sg.Push()],
        ]

        self.janela = sg.Window("Lista de tipos de caixa", layout, finalize=True)

        while True:
            evento, valores = self.abrir_janela()
            if evento in (None, "Ok"):
                break

        self.fechar_janela()
