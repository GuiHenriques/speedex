from telas.tela_funcionario import TelaFuncionario
from entidades.modelos.funcionario import Funcionario
from entidades.repositorios.funcionario_repositorio import FuncionarioRepositorio
from utils.valildadores import cpf_validador
from utils.formatadores import cpf_formatador
from utils.valildadores import email_validador
from utils.valildadores import campo_vazio_validador

import hashlib

class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__tela = TelaFuncionario() if not controlador_sistema.development_mode else None
        self.__repositorio = FuncionarioRepositorio(controlador_sistema)

    @property
    def tela_funcionario(self):
        return self.__tela

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
                self.tela_funcionario.mensagem("Erro", "Login ou senha incorreto.")

    def abre_tela_cadastro(self):
        while True:
            evento, valores = self.__tela.tela_cadastro()

            if valores == None or evento == "login":
                return False

            if campo_vazio_validador(valores):
                self.tela_funcionario.mensagem("Erro", "Por favor, preencha todos os campos.")
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
        
    def mensagem(self, mensagem):
        try:
            self.tela_funcionario.mensagem(mensagem)
        except AttributeError as e: # Quando em ambiente de teste, já que None vai chamar o método mensagem.
            pass

    def cadastrar_funcionario(self, cpf: str, nome: str, email: str, senha: str) -> bool:
        if not cpf_validador(cpf):
            self.mensagem("Erro", "CPF inválido.")
            return False

        if not email_validador(email):
            self.tela_funcionario.mensagem("Erro", "Email inválido.")
            return False

        if self.__verificar_se_cpf_existe(cpf):
            self.__tela.mensagem("Erro", "CPF já cadastrado.")
            return False

        if self.__verificar_se_email_existe(email):
            self.__tela.mensagem("Erro", "Email já cadastrado.")
            return False

        hash_senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        cpf_formatado = cpf_formatador(cpf)
        novo_funcionario = Funcionario(cpf_formatado, nome, email, hash_senha)
        cadastrado, msg_error = self.__repositorio.registrar_funcionario(novo_funcionario)
        if cadastrado:
            self.mensagem("Funcionário cadastrado com sucesso.")
            return novo_funcionario
        else:
            self.tela_funcionario.mensagem("Não foi possível cadastrar o funcionário", msg_error)
            return False
