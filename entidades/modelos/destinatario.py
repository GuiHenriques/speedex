from entidades.modelos.pessoa import Pessoa
from entidades.modelos.endereco import Endereco


class Destinatario(Pessoa):
    def __init__(self, cpf: str, nome: str, endereco: Endereco):
        super().__init__(cpf, nome)
        self.__endereco = endereco

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
