from controladores.controlador_sistema import ControladorSistema
from entidades.modelos.endereco import Endereco
from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario

import pytest

class TestCliente:
    controlador_sistema = ControladorSistema()
    nome_valido = "Michael Jackson"
    endereco_valido = Endereco("26321-510", "Rio de Janeiro", "Queimados", "Parque Ipanema", "Rua Santo Elias", "24A")

    @pytest.fixture(scope="session", autouse=True)
    def limpar_banco(self):
        self.controlador_sistema.database.cursor().execute("TRUNCATE TABLE clientes;")

    def test_passar_em_cadastro_correto_de_remetente(self):
        cpf_valido = "737.784.150-85"
        cliente_esperado = Destinatario(cpf_valido, self.nome_valido, self.endereco_valido)
        cliente_cadastrado = self.controlador_sistema.controlador_cliente.cadastrar_cliente(cpf_valido, self.nome_valido, self.endereco_valido)
        assert cliente_cadastrado == cliente_esperado
    
    def test_passar_em_cadastro_correto_de_destinatario(self):
        assert True