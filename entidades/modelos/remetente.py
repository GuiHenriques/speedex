from typing import Any
from entidades.modelos.pessoa import Pessoa


class Remetente(Pessoa):
    def __init__(self, cpf: str, nome: str):
        super().__init__(cpf, nome)

    def __eq__(self, other):
        if isinstance(other, Remetente):
            return self.cpf == other.cpf and self.nome == other.nome
        else:
            return False
        
    def __str__(self):
        return f"Remetente: {self.nome} | CPF: {self.cpf}"