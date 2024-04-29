

class Caixa:
    def __init__(self, largura, altura, comprimento):
        self._largura = largura
        self._altura = altura
        self._comprimento = comprimento
 

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, largura):
        self._largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def comprimento(self):
        return self._comprimento

    @comprimento.setter
    def comprimento(self, comprimento):
        self._comprimento = comprimento


