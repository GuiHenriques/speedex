from entidades.modelos.pessoa import Pessoa


class Remetente(Pessoa):
    def __init__(self, cpf: str, nome: str):
        super().__init__(cpf, nome)
