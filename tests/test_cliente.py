from controladores.controlador_sistema import ControladorSistema

import pytest

class TestCliente:
    controlador_sistema = ControladorSistema()
    nome_valido = "Michael Jackson"

    @pytest.fixture(scope="session", autouse=True)
    def limpar_banco(self):
        self.controlador_sistema.database.cursor().execute("TRUNCATE TABLE clientes;")

    def test_passar_em_cadastro_correto(self):
        ...