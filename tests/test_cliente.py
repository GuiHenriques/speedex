from entidades.modelos.endereco import Endereco
from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario
from tests.conftest import controlador_sistema as cs

import pytest

class TestCliente:
    controlador_sistema = cs
    nome_valido = "Michael Jackson"
    endereco_valido = Endereco("26321510", "Rio de Janeiro", "Queimados", "Parque Ipanema", "Rua Santo Elias", "24A")

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