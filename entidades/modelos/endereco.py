from utils.formatadores import cep_formatador


class Endereco:
    def __init__(self, cep: str, estado: str, cidade: str, bairro: str, rua: str, numero: str):
        self.__cep = cep_formatador(cep)
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def __str__(self):
        return f"CEP: {self.__cep},\
                 Estado: {self.__estado},\
                 Cidade: {self.__cidade},\
                 Bairro: {self.__bairro},\
                 Rua: {self.__rua},\
                 Número: {self.__numero}"

    def __eq__(self, other):
        if isinstance(other, Endereco):
            return self.cep == other.cep and self.estado == other.estado and self.cidade == other.cidade\
                and self.bairro == other.bairro and self.rua == other.rua and self.numero == other.numero
        else:
            return False