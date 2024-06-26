from telas.tela_sistema import TelaSistema
from controladores.controlador_funcionario import ControladorFuncionario
from controladores.controlador_tipo_de_entrega import ControladorTipoDeEntrega
from controladores.controlador_tipo_de_caixa import ControladorTipoDeCaixa
from controladores.controlador_entrega import ControladorEntrega
from controladores.controlador_cliente import ControladorCliente
from controladores.controlador_relatorio import ControladorRelatorio

from entidades.modelos.funcionario import Funcionario

import os
import sys
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class ControladorSistema:
    def __init__(self):
        self.__tela = TelaSistema()
        self.__database = psycopg2.connect(os.getenv(self.get_connection_string()))
        self.__session: Funcionario = None
        self.__database.autocommit = True  # Realiza commit no banco sempre depois de executar uma query (psycopg2).
        self.__development_mode = not self.modo_producao()
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_tipo_de_entrega = ControladorTipoDeEntrega(self)
        self.__controlador_tipo_de_caixa = ControladorTipoDeCaixa(self)
        self.__controlador_entrega = ControladorEntrega(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_relatorio = ControladorRelatorio(self)

    @property
    def database(self):
        return self.__database

    @property
    def session(self):
        return self.__session

    @property
    def development_mode(self):
        return self.__development_mode

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega

    @property
    def controlador_tipo_de_caixa(self):
        return self.__controlador_tipo_de_caixa

    @property
    def controlador_entrega(self):
        return self.__controlador_entrega

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def inicializa_sistema(self):
        self.__session = self.login()
        if not self.__session:
            return

        self.abre_tela()

    def login(self):
        return self.__controlador_funcionario.abre_tela_login()

    def menu_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega.abre_tela()

    def menu_tipo_de_caixa(self):
        return self.__controlador_tipo_de_caixa.abre_tela()

    def menu_entrega(self):
        return self.__controlador_entrega.dados_entrega()

    def menu_cliente(self):
        return self.__controlador_cliente.abre_tela()

    def menu_relatorio(self):
        return self.__controlador_relatorio.abre_tela()

    def encerra_sistema(self):
        self.__database.close()
        exit()

    def modo_producao(self):
        return "main.py" in sys.argv[0]

    def get_connection_string(self):
        if self.modo_producao():
            return "DB_CONNECTION_STRING"
        else:
            return "DB_TEST_CONNECTION_STRING"

    def abre_tela(self):
        lista_opcoes = {
            1: self.menu_entrega,
            2: self.menu_cliente,
            3: self.menu_tipo_de_entrega,
            4: self.menu_tipo_de_caixa,
            5: self.menu_relatorio,
            0: self.encerra_sistema,
        }

        while True:
            opcao = self.__tela.abre_tela()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
