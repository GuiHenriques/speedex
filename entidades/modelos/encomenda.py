from entidades.modelos.tipo_de_caixa import TipoDeCaixa

class Encomenda:

    def __init__(self, conteudo: str, peso: int, tipo_de_caixa: TipoDeCaixa):
        self.__id = None
        self.__conteudo = conteudo
        self.__peso = peso
        self.__tipo_de_caixa = tipo_de_caixa

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def conteudo(self):
        return self.__conteudo
    
    @conteudo.setter
    def conteudo(self, conteudo):
        self.__conteudo = conteudo

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def tipo_de_caixa(self):
        return self.__tipo_de_caixa
    
    @tipo_de_caixa.setter
    def tipo_de_caixa(self, tipo_de_caixa):
        self.__tipo_de_caixa = tipo_de_caixa

    def __str__(self):
        return f"Conteúdo: {self.conteudo} - Peso {self.peso} - Tipo de caixa: {self.tipo_de_caixa}"