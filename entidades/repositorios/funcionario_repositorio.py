from entidades.modelos.funcionario import Funcionario

from psycopg2 import extensions

class FuncionarioRepositorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_funcionario(self, funcionario: Funcionario):
        try:
            self.__cursor.execute(f"INSERT INTO funcionarios(cpf, nome, email, senha)\
                                VALUES ('{funcionario.cpf}', '{funcionario.nome}', '{funcionario.email}', '{funcionario.senha}');")
            self.__controlador_sistema.database.commit()
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    # busca um funcionario no banco de dados por email ou cpf
    def pegar_funcionario(self, email_ou_cpf):
        dados_funcionario: tuple = None
        try:
            self.__cursor.execute(f"SELECT * FROM Funcionarios\
                                  WHERE cpf='{email_ou_cpf}' OR email='{email_ou_cpf}'")
            dados_funcionario = self.__cursor.fetchone()
        except Exception as e:
            print(e)
        
        if dados_funcionario != None:
            funcionario = Funcionario(*dados_funcionario)
            return funcionario
    
    # busca a senha de um funcionario no banco de dados por email
    def pegar_senha(self, email):
        senha: str = None
        try:
            self.__cursor.execute(f"SELECT senha FROM Funcionarios WHERE email='{email}'")
            senha = self.__cursor.fetchone()
        except Exception as e:
            print(e)
        
        if senha != None:
            return senha[0]