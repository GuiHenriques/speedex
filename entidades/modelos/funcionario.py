from entidades.modelos.pessoa import Pessoa
import hashlib

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, email, senha):
        super().__init__(cpf, nome)
        self.__email = email
        self.__senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha_hash(self):
        return self.__senha_hash
    
    @senha_hash.setter
    def senha(self, senha):
        self.__senha_hash = senha

    def __eq__(self, other):
        if other is not None:
            return self.cpf == other.cpf and self.nome == other.nome\
                and self.email == other.email and self.senha_hash == other.senha_hash
        else:
            return False