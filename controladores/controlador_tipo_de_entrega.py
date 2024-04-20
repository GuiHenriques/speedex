from telas.tela_tipo_de_entrega import TelaTiposDeEntrega


class ControladorTiposDeEntrega:
    def __init__(self):
        self.__tela_tipo_de_entrega = TelaTiposDeEntrega(self)

    def abre_tela(self):
        while True:
            valores = self.__tela_tipo_de_entrega.abre_tela()
            if valores == None:
                return False
            else:
                self.__tela_tipo_de_entrega.mensagem("Tipo de entrega cadastrado com sucesso!")
