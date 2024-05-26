from abc import ABC
from utils.formatadores import cpf_formatador

class Pessoa(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf_formatador(cpf)
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome