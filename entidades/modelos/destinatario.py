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

    def __eq__(self, other):
        if isinstance(other, Destinatario):
            return self.cpf == other.cpf and self.nome == other.nome and self.endereco == other.endereco
        else:
            return False
