

class tipoDeEntrega:
    def __init__(self, id, nome, taxa, descricao):
        self._id = id
        self._nome = nome
        self._taxa = taxa
        self._descricao = descricao
 

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
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao


