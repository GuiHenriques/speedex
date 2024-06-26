from entidades.modelos.endereco import Endereco
from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario
from tests.conftest import controlador_sistema as cs

import pytest

class TestCliente:
    controlador_sistema = cs
    nome_valido = "Michael Jackson"
    endereco_valido = Endereco("26321-510", "Rio de Janeiro", "Queimados", "Parque Ipanema", "Rua Santo Elias", "24A")

    @pytest.fixture(scope="class", autouse=True)
    def limpar_banco(self):
        self.controlador_sistema.database.cursor().execute("TRUNCATE TABLE clientes;")

    def test_passar_em_cadastro_correto_de_remetente(self):
        cpf_valido = "561.656.780-92"
        cliente_esperado = Remetente(cpf_valido, self.nome_valido)
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(
            cpf_valido, self.nome_valido
        )
        assert cliente_cadastrado == cliente_esperado

    def test_passar_em_cadastro_correto_de_destinatario(self):
        cpf_valido = "737.784.150-85"
        cliente_esperado = Destinatario(cpf_valido, self.nome_valido, self.endereco_valido)
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(
            cpf_valido, self.nome_valido, self.endereco_valido
        )
        assert cliente_cadastrado == cliente_esperado

    def test_falhar_em_cadastro_com_cpf_invalido(self):
        cpf_invalido = "123.456.789-10"
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(
            cpf_invalido, self.nome_valido
        )
        assert not cliente_cadastrado

    def test_falhar_em_cadastro_com_cpf_ja_cadastrado(self):
        cpf_valido = "689.993.210-53"
        self.controlador_sistema.controlador_cliente.cadastrar_cliente(cpf_valido, self.nome_valido)
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(
            cpf_valido, self.nome_valido
        )
        assert not cliente_cadastrado

    def test_sucesso_em_exclusao_de_remetente(self):
        cpf_valido = "738.933.010-46"
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(
            cpf_valido, self.nome_valido
        )
        cliente_excluido = self.controlador_sistema.controlador_cliente.excluir_cliente(cpf_valido)
        if isinstance(cliente_excluido, Remetente):
            assert cliente_excluido == cliente_cadastrado
        else:
            assert False

    def test_sucesso_em_exclusao_de_destinatario(self):
        cpf_valido = "658.512.530-45"
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(
            cpf_valido, self.nome_valido, self.endereco_valido
        )
        cliente_excluido = self.controlador_sistema.controlador_cliente.excluir_cliente(cpf_valido)
        if isinstance(cliente_excluido, Destinatario):
            assert cliente_excluido == cliente_cadastrado
        else:
            assert False

    def test_falhar_em_exclusao_de_cpf_invalido(self):
        cpf_invalido = "123.456.789-10"
        cliente_excluido = self.controlador_sistema.controlador_cliente.excluir_cliente(cpf_invalido)
        assert not cliente_excluido

    def test_falhar_em_exclusao_de_cliente_inexistente(self):
        cpf_valido = "482.061.170-40"
        cliente_excluido = self.controlador_sistema.controlador_cliente.excluir_cliente(cpf_valido)
        assert not cliente_excluido