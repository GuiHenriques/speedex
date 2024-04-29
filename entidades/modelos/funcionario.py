from entidades.modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, email, senha):
        super().__init__(cpf, nome)
        self.__email = email
        self.__senha = senha

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha