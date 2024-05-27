from telas.tela_funcionario import TelaFuncionario
from entidades.modelos.funcionario import Funcionario
from entidades.repositorios.funcionario_repositorio import FuncionarioRepositorio
from utils.valildadores import cpf_validador
from utils.formatadores import cpf_formatador
from utils.valildadores import email_validador
from utils.valildadores import algum_campo_e_vazio

import hashlib

class ControladorFuncionario:
    def __init__(self, controlador_sistema):
        self.__tela = TelaFuncionario() if not controlador_sistema.development_mode else None
        self.__repositorio = FuncionarioRepositorio(controlador_sistema)

    @property
    def tela(self):
        return self.__tela

    def abre_tela_login(self):
        while True:
            evento, valores = self.__tela.tela_login()

            if valores == None:
                return False

            if evento == "cadastro":
                self.abre_tela_cadastro()
                continue

            funcionario_logado = self.verificar_login(valores["email"], valores["senha"])
            if funcionario_logado:
                return funcionario_logado
            else:
                self.__tela.mensagem("Login ou senha incorreto.")

    def abre_tela_cadastro(self):
        while True:
            evento, valores = self.__tela.tela_cadastro()

            if valores == None or evento == "login":
                return False

            if algum_campo_e_vazio(valores):
                self.__tela.mensagem("Por favor, preencha todos os campos.")
                continue

            if self.cadastrar_funcionario(valores["cpf"], valores["nome"], valores["email"], valores["senha"]):
                break

    def verificar_login(self, email: str, senha: str) -> Funcionario | bool:
        funcionario = self.__repositorio.pegar_funcionario(email)

        if funcionario == None: # email não encontrado
            return False

        # hash da senha para comparar com o hash armazenado
        senha_hash_fornecida = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        if senha_hash_fornecida == funcionario.senha_hash:
            return funcionario
        else:
            return False

    def cadastrar_funcionario(self, cpf: str, nome: str, email: str, senha: str) -> bool:
        
        if not cpf_validador(cpf):
            self.__mensagem("CPF inválido.")
            return False

        if not email_validador(email):
            self.__mensagem("Email inválido.")
            return False

        # Criando funcionario com cpf e emails validos.
        senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        novo_funcionario = Funcionario(cpf, nome, email, senha_hash)

        if self.__cpf_existe(novo_funcionario.cpf):
            self.__mensagem("CPF já cadastrado.")
            return False

        if self.__verificar_se_email_existe(novo_funcionario.email):
            self.__mensagem("Email já cadastrado.")
            return False

        cadastrado, msg_error = self.__repositorio.registrar_funcionario(novo_funcionario)
        if cadastrado:
            self.__mensagem("Funcionário cadastrado com sucesso.")
            return novo_funcionario
        else:
            self.__mensagem(f"Não foi possível cadastrar o funcionário:\n{msg_error}")
            return False

    def __cpf_existe(self, cpf: str):
        if self.__repositorio.pegar_funcionario(cpf) == None:
            return False
        else:
            return True

    def __verificar_se_email_existe(self, email: str) -> bool:
        if self.__repositorio.pegar_funcionario(email) == None:
            return False
        else:
            return True
        
    def __mensagem(self, mensagem):
        try:
            self.__tela.mensagem(mensagem)
        except AttributeError as e: # Quando em ambiente de teste, já que None vai chamar o método mensagem.
            pass