from entidades.modelos.caixa import Caixa


class TipoDeCaixa:
    def __init__(self, nome: str, taxa: float, dimensoes: Caixa, id: int = None):
        self.__id = id
        self.__nome = nome
        self.__taxa = taxa
        self.__dimensoes = dimensoes

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def taxa(self):
        return self.__taxa

    @taxa.setter
    def taxa(self, taxa):
        self.__taxa = taxa

    @property
    def dimensoes(self):
        return self.__dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self.__dimensoes = dimensoes

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Taxa: {self.__taxa} | Dimensões: {self.__dimensoes}"
