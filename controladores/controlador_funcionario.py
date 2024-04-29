from telas.tela_funcionario import TelaFuncionario
from entidades.modelos.funcionario import Funcionario
from entidades.repositorios.funcionario_repositorio import FuncionarioRepositorio
from utils.valildadores import cpf_validador
from utils.formatadores import cpf_formatador
from utils.valildadores import email_validador

import hashlib

class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__tela_funcionario = TelaFuncionario()
        self.__repositorio = FuncionarioRepositorio(controlador_sistema)

    @property
    def tela_funcionario(self):
        return self.__tela_funcionario

    def abre_tela_login(self):
        while True:
            evento, valores = self.tela_funcionario.tela_login()

            if valores == None:
                return False

            if evento == "cadastro":
                self.abre_tela_cadastro()
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

            if self.cadastrar_funcionario(valores["cpf"], valores["nome"], valores["email"], valores["senha"]):
                break

    def verificar_login(self, email, senha):
        funcionario = self.__repositorio.pegar_funcionario(email)
        
        if funcionario == None: # email não encontrado
            return False
        
        # hash da senha para comparar com o hash armazenado
        senha_hash_fornecida = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        return senha_hash_fornecida == funcionario.senha

    # itera por todos os valores recebidos na tela para verificar se nenhum deles é vazio.
    def verificar_campo_vazio(self, valores):
        if any(value.strip() == "" for value in valores.values()):
            return True
        return False

    def __verificar_se_cpf_existe(self, cpf: str):
        if self.__repositorio.pegar_funcionario(cpf) == None:
            return False
        else:
            return True

    def __verificar_se_email_existe(self, email: str) -> bool:
        if self.__repositorio.pegar_funcionario(email) == None:
            return False
        else:
            return True

    def cadastrar_funcionario(self, cpf: str, nome: str, email: str, senha: str) -> bool:
        if not cpf_validador(cpf):
            self.tela_funcionario.mensagem("CPF inválido.")
            return False
        
        if not email_validador(email):
            self.tela_funcionario.mensagem("Email inválido.")
            return False

        if self.__verificar_se_cpf_existe(cpf):
            self.__tela_funcionario.mensagem("CPF já cadastrado.")
            return False

        if self.__verificar_se_email_existe(email):
            self.__tela_funcionario.mensagem("Email já cadastrado.")
            return False

        hash_senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        cpf_formatado = cpf_formatador(cpf)
        novo_funcionario = Funcionario(cpf_formatado, nome, email, hash_senha)
        cadastrado, msg_error = self.__repositorio.registrar_funcionario(novo_funcionario)
        if cadastrado:
            self.tela_funcionario.mensagem("Funcionário cadastrado com sucesso.")
            return True
        else:
            self.tela_funcionario.mensagem(f"Não foi possível cadastrar o funcionário:\n{msg_error}")
            return False
