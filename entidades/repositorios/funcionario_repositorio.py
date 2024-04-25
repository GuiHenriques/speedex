from entidades.modelos.funcionario import Funcionario

from psycopg2 import extensions
from psycopg2.errors import UniqueViolation

class FuncionarioRepositorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_no_banco(self, funcionario: Funcionario):
        try:
            self.__cursor.execute(f"INSERT INTO funcionarios(cpf, nome, email, senha)\
                                VALUES ('{funcionario.cpf}', '{funcionario.nome}', '{funcionario.email}', '{funcionario.senha}');")
            self.__controlador_sistema.database.commit()
        except UniqueViolation as e:
            if "cpf" in str(e):
                return False, "CPF já cadastrado."
            elif "email" in str(e):
                return False, "Email já cadastrado."

        return True, ""