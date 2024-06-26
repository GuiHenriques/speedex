from .remetente import Remetente
from .destinatario import Destinatario
from .encomenda import Encomenda
from .tipo_de_entrega import tipoDeEntrega
from .funcionario import Funcionario


class Entrega:
    def __init__(
        self,
        remetente: Remetente,
        destinatario: Destinatario,
        encomenda: Encomenda,
        tipo_de_entrega: tipoDeEntrega,
        funcionario: Funcionario,
        distancia: float,
        valor: float,
        tempo: str,
    ):
        self.__id = None
        self.__remetente = remetente
        self.__destinatario = destinatario
        self.__encomenda = encomenda
        self.__tipo_de_entrega = tipo_de_entrega
        self.__funcionario = funcionario
        self.__distancia = distancia
        self.__valor = valor
        self.__tempo = tempo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def remetente(self):
        return self.__remetente

    @remetente.setter
    def remetente(self, remetente):
        self.__remetente = remetente

    @property
    def destinatario(self):
        return self.__destinatario

    @destinatario.setter
    def destinatario(self, destinatario):
        self.__destinatario = destinatario

    @property
    def encomenda(self):
        return self.__encomenda

    @encomenda.setter
    def encomenda(self, encomenda):
        self.__encomenda = encomenda

    @property
    def tipo_de_entrega(self):
        return self.__tipo_de_entrega

    @tipo_de_entrega.setter
    def tipo_de_entrega(self, tipo_de_entrega):
        self.__tipo_de_entrega = tipo_de_entrega

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, tempo):
        self.__tempo = tempo

    def __str__(self):
        return f"ENTREGA = Remetente: {self.remetente.nome} - Destinatário: {self.destinatario.nome} - Encomenda: {self.encomenda} - Tipo de entrega: {self.tipo_de_entrega} - Funcionário: {self.funcionario} - Distância: {self.distancia}"