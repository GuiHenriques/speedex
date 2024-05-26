

class tipoDeEntrega:
    def __init__(self, id, nome, taxa: float, descricao, velocidade: int):
        self._id = id
        self._nome = nome
        self._taxa = taxa
        self._descricao = descricao
        self._velocidade = velocidade
 

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

    @property
    def velocidade(self):
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self._velocidade = velocidade

    def __str__(self):
        return f"ID: {self.id} - Tipo de entrega: {self._nome} - Taxa: {self._taxa} - Descrição: {self._descricao} - Velocidade: {self._velocidade}"
