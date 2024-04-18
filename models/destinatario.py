from pessoa import Pessoa
from endereco import Endereco


class Destinatario(Pessoa):
    def __init__(self, nome, cpf, endereco: Endereco):
        super().__init__(nome, cpf)
        self._endereco = endereco

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
