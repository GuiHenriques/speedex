from telas.telaAbstrata import TelaAbstrata
from utils.valildadores import algum_campo_e_vazio

import PySimpleGUI as sg

class TelaTiposDeEntrega(TelaAbstrata):
    def __init__(self, ControladorTipoDeEntrega):
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
        self.janela = sg.Window("Menu de tipos de entrega", layout, finalize=True)

    def pega_dados_tipo_de_entrega(self):

        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        layout = [
            [sg.Text("Nome: ", size=(11, 1)), sg.InputText("", key="nome")],
            [sg.Text("Taxa (0-100%): ", size=(11, 1)), sg.InputText("", key="taxa")],
            [sg.Text("Descrição: ", size=(11, 1)), sg.InputText("", key="descricao")],
            [sg.Text("Selecione uma velocidade de entrega: ")],
            [sg.Radio("Entrega econômica", "Radio1", key="0", default=True)],
            [sg.Radio("Entrega normal", "Radio1", key="1")],
            [sg.Radio("Entrega rápida", "Radio1", key="2")],
            [sg.Radio("Entrega expressa", "Radio1", key="3")],
            [sg.Push(), sg.Button("Cadastrar"), sg.Cancel("Cancelar")],
        ]

        self.janela = sg.Window("Cadastro de tipos de entrega", layout)
        evento , valores = self.abrir_janela()
        entrada_invalida = False

        if evento in (None, "Cancelar"):
            self.fechar_janela()
            return

        if algum_campo_e_vazio(valores):
            sg.popup("Você deve preencher todos os campos!")
            self.fechar_janela()
            entrada_invalida = True
            return

        if not is_float(valores["taxa"]):
            sg.popup("A taxa deve ser um número válido!")
            self.fechar_janela()
            entrada_invalida = True
            return

        self.fechar_janela()
        if entrada_invalida:
            return
        else:
            # Encontrando a chave cujo valor é True
            velocidades = ['0', '1', '2', '3']
            for velocidade in velocidades:
                if valores.get(velocidade) is True:
                    indice = velocidade
                    break

            return {
                "nome": valores["nome"],
                "taxa": float(valores["taxa"]),
                "descricao": valores["descricao"],
                "velocidade": int(indice)
            }

    def seleciona_codigo_tipo_de_entrega(self):
        layout = [
            [sg.Text("Código: "), sg.InputText("", key="codigo")],
            [sg.Push(), sg.Button("Confirmar"), sg.Cancel("Cancelar")],
        ]
        self.janela = sg.Window("Selecionar código de um tipo de entrega", layout)
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

    def mostra_tipo_de_entrega(self, resultados):
        string_resultados=""
        if not resultados:
            string_resultados = "Nenhum tipo de entrega cadastrado!"
        else:
            for row in resultados:
                string_resultados += f"Código:{row[0]} \nNome: {row[1]} \nTaxa: {row[2]}% \nDescrição: {row[3]}\n \n"

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

        self.janela = sg.Window("Lista de tipos de entrega", layout, finalize=True)

        while True:
            evento, valores = self.abrir_janela()
            if evento in (None, "Ok"):
                break

        self.fechar_janela()
