class Endereco:
    def __init__(self, cep: str, estado: str, cidade: str, bairro: str, rua: str, numero: str):
        self._cep = cep
        self._estado = estado
        self._cidade = cidade
        self._bairro = bairro
        self._rua = rua
        self._numero = numero

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, rua):
        self._rua = rua

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    def __str__(self):
        return f"CEP: {self._cep},\
                 Estado: {self._estado},\
                 Cidade: {self._cidade},\
                 Bairro: {self._bairro},\
                 Rua: {self._rua},\
                 Número: {self._numero}"

    def __eq__(self, other):
        if isinstance(other, Endereco):
            return self.cep == other.cep and self.estado == other.estado and self.cidade == other.cidade\
                and self.bairro == other.bairro and self.rua == other.rua and self.numero == other.numero
        else:
            return False