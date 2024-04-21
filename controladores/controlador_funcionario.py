from telas.tela_funcionario import TelaFuncionario
from entidades.funcionario import Funcionario

from psycopg2 import extensions
import hashlib

class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    @property
    def tela_funcionario(self):
        return self.__tela_funcionario

    def abre_tela_login(self):
        while True:
            evento, valores = self.tela_funcionario.tela_login()

            if valores == None:
                return False

            if evento == "cadastro":
                if self.abre_tela_cadastro():
                    return True
                continue

            if self.verificar_login(valores["email"], valores["senha"]):
                return True
            else:
                self.tela_funcionario.mensagem("Login ou senha incorreto.")

    def abre_tela_cadastro(self):
        while True:
            evento, valores = self.__tela_funcionario.tela_cadastro()

            if valores == None or evento == "login":
                return False

            if self.verificar_campo_vazio(valores):
                self.tela_funcionario.mensagem("Por favor, preencha todos os campos.")
                continue

            else:
                self.cadastrar_funcionario(
                    valores["cpf"], valores["nome"], valores["email"], valores["senha"]
                )
                return True

    def verificar_login(self, email, senha):
        self.__cursor.execute(f"SELECT senha FROM funcionarios WHERE email = '{email}';")
        senha_hash_armazenada = self.__cursor.fetchone()

        # email não encontrado
        if not senha_hash_armazenada:
            return False

        # hash da senha para comparar com o hash armazenado
        senha_hash_fornecida = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        return senha_hash_fornecida == senha_hash_armazenada[0]


    def verificar_campo_vazio(self, valores):
        if any(value.strip() == "" for value in valores.values()):
            return True
        return False

    def cadastrar_funcionario(self, cpf: str, nome: str, email: str, senha: str):        
        hash_senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        self.__cursor.execute(f"INSERT INTO funcionarios(cpf, nome, email, senha)\
                              VALUES ('{cpf}', '{nome}', '{email}', '{hash_senha}');")

        self.__controlador_sistema.database.commit()
        self.tela_funcionario.mensagem("Funcionário cadastrado com sucesso.")
        return True
