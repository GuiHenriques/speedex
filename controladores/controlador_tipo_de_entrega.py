from telas.tela_tipo_de_entrega import TelaTiposDeEntrega


class ControladorTipoDeEntrega:
    def __init__(self):
        self.__tela_tipo_de_entrega = TelaTiposDeEntrega(self)

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_tipo_de_entrega,
            2: self.alterar_tipo_de_entrega,
            3: self.excluir_tipo_de_entrega,
            0: "Retornar para menu principal",
        }

        while True:
            opcao = self.__tela_tipo_de_entrega.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
    
    def incluir_tipo_de_entrega(self):
        dados_tipo_de_entrega = self.__tela_tipo_de_entrega.pega_dados_tipo_de_entrega()
        if dados_tipo_de_entrega == None:
            return
        
    def alterar_tipo_de_entrega(self):
        codigo_selecionado = self.__tela_tipo_de_entrega.seleciona_codigo_tipo_de_entrega()
        
    def excluir_tipo_de_entrega(self):
        codigo_selecionado = self.__tela_tipo_de_entrega.seleciona_codigo_tipo_de_entrega()