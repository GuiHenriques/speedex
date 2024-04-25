from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, cpf, nome):
        self._nome = nome
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf