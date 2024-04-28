from telas.tela_encomenda import TelaEncomenda

class ControladorEncomenda:
    def __init__(self, controlador_sistema):
        self.__tela_encomenda = TelaEncomenda()
        self.__controlador_sistema = controlador_sistema

    @property
    def tela_encomenda(self):
        return self.__tela_encomenda
    
    def abre_tela_encomenda(self):
        while True:
            valores = self.tela_encomenda.tela_encomenda()

            if valores == None:
                return False
            