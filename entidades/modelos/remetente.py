from entidades.modelos.pessoa import Pessoa


class Remetente(Pessoa):
    def __init__(self, cpf: str, nome: str):
        super().__init__(cpf, nome)

    def __eq__(self, other):
        if isinstance(other, Remetente):
            return self.cpf == other.cpf and self.nome == other.nome
        else:
            return False