from controladores.controlador_sistema import ControladorSistema
from entidades.modelos.funcionario import Funcionario
from tests.conftest import controlador_sistema as cs

import pytest
import hashlib


class TestFuncionario:
    controlador_sistema = cs
    nome_valido = "Taylor Swift"
    senha_valida = "123"
    senha_hash = hashlib.sha256(senha_valida.encode('utf-8')).hexdigest()

    # Sempre antes de realizar a bateria de testes de funcionário, ele limpa a tabela de funcionários
    @pytest.fixture(scope="class", autouse=True)
    def limpar_banco(self):
        self.controlador_sistema.database.cursor().execute("TRUNCATE TABLE funcionarios;")

    def test_passar_em_cadastro_correto(self):
        cpf_valido = "909.580.950-19"
        email_valido = "emailvalido1@gmail.com"
        funcionario_esperado = Funcionario(cpf_valido, self.nome_valido, email_valido, self.senha_hash)
        funcionario_cadastrado = self.controlador_sistema.controlador_funcionario.cadastrar_funcionario(
            cpf_valido, self.nome_valido, email_valido, self.senha_valida
        )
        assert funcionario_cadastrado == funcionario_esperado

    def test_falhar_cadastro_com_cpf_invalido(self):
        cpf_invalido = "123456789"
        email_valido = "emailvalido3@gmail.com"

        funcionario_cadastrado = self.controlador_sistema.controlador_funcionario.cadastrar_funcionario(
            cpf_invalido, self.nome_valido, email_valido, self.senha_hash
        )
        assert not funcionario_cadastrado

    def test_falhar_cadastro_com_cpf_ja_cadastrado(self):
        cpf_repetido = "627.975.840-07"
        email_valido = "emailvalido3@gmail.com"
        email_valido2 = "segundoemailvalido3@gmail.com"

        self.controlador_sistema.controlador_funcionario.cadastrar_funcionario(
            cpf_repetido, self.nome_valido, email_valido, self.senha_hash
        )

        funcionario_repetido_cadastrado = self.controlador_sistema.controlador_funcionario.cadastrar_funcionario(
            cpf_repetido, self.nome_valido, email_valido2, self.senha_hash
        )
        assert not funcionario_repetido_cadastrado

    def test_falhar_cadastro_com_email_ja_cadastrado(self):
        cpf_valido = "991.889.610-87"
        cpf_valido2 = "852.211.990-25"
        email_repetido = "emailrepetido@email.com"

        self.controlador_sistema.controlador_funcionario.cadastrar_funcionario(
            cpf_valido, self.nome_valido, email_repetido, self.senha_hash
        )

        funcionario_repetido_cadastrado = self.controlador_sistema.controlador_funcionario.cadastrar_funcionario(
            cpf_valido2, self.nome_valido, email_repetido, self.senha_hash
        )

        assert not funcionario_repetido_cadastrado