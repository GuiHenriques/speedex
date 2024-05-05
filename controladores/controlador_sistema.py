from telas.tela_sistema import TelaSistema
from controladores.controlador_funcionario import ControladorFuncionario
from controladores.controlador_tipo_de_entrega import ControladorTipoDeEntrega
from controladores.controlador_encomenda import ControladorEncomenda
from controladores.controlador_cliente import ControladorCliente

import os, sys
import psycopg2
from dotenv import load_dotenv
load_dotenv()

class ControladorSistema:
    def __init__(self):
        self.__tela = TelaSistema()
        self.__database = psycopg2.connect(os.getenv(self.get_connection_string()))
        self.__database.autocommit = True # Realiza commit no banco sempre depois de executar uma query (psycopg2).
        self.__development_mode = not self.modo_producao()
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_tipo_de_entrega = ControladorTipoDeEntrega(self)
        self.__controlador_encomenda = ControladorEncomenda(self)
        self.__controlador_cliente = ControladorCliente(self)

    @property
    def database(self):
        return self.__database

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
    def controlador_encomenda(self):
        return self.__controlador_encomenda
    
    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def inicializa_sistema(self):
        # if not self.login():
        #     return

        self.abre_tela()

    def abre_tela(self):
        self.__tela.abre_tela()

    def login(self):
        return self.__controlador_funcionario.abre_tela_login()

    def menu_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega.abre_tela()
    
    def menu_encomenda(self):
        return self.__controlador_encomenda.abre_tela_encomenda()
    
    def menu_cliente(self):
        return self.__controlador_cliente.abre_tela()
    
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
            1: self.menu_encomenda,
            2: self.menu_cliente,
            3: self.menu_tipo_de_entrega,
            0: self.encerra_sistema,
        }
        # Tipos de Entrega 1
        # Tipos de Caixa 2
        # Clientes 3
        # Encomendas 4 
        # Entregas 5
        # Relatórios 6 

        while True:
            opcao = self.__tela.abre_tela()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()