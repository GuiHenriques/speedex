from telas.tela_entrega import TelaEntrega
from entidades.repositorios.entrega_repositorio import EntregaRepositorio

class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela_entrega = TelaEntrega() if not controlador_sistema.development_mode else None
        self.__repositorio_entrega = EntregaRepositorio(controlador_sistema)

    @property
    def tela_entrega(self):
        return self.__tela_entrega
    
    def abre_tela_entrega(self):
        while True:
            evento, valores = self.tela_entrega.tela_entrega()

            if valores == None:
                return False

    