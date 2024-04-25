from entidades.modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, email, senha):
        super().__init__(nome, cpf)
        self._email = email
        self._senha = senha

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha