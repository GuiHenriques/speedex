from entidades.modelos.caixa import Caixa

class TipoDeCaixa:
    def __init__(self, nome: str, taxa: float, dimensoes: Caixa):
        self._id = None
        self._nome = nome
        self._taxa = taxa
        self._dimensoes = dimensoes

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def taxa(self):
        return self._taxa

    @taxa.setter
    def taxa(self, taxa):
        self._taxa = taxa

    @property
    def dimensoes(self):
        return self._dimensoes

    @dimensoes.setter
    def dimensoes(self, dimensoes):
        self._dimensoes = dimensoes

    def __str__(self):
        return f"ID: {self.id} | Nome: {self._nome} | Taxa: {self._taxa} | Dimensões: {self._dimensoes}"