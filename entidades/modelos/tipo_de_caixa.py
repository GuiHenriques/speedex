from entidades.modelos.caixa import Caixa

class TipoDeCaixa:
    def __init__(self, nome: str, taxa: float, dimensoes: Caixa):
        self.__id = None
        self.__nome = nome
        self.__taxa = taxa
        # super().__init__(dimensoes)