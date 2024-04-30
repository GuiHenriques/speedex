from telas.tela_sistema import TelaSistema
from controladores.controlador_funcionario import ControladorFuncionario
from controladores.controlador_tipo_de_entrega import ControladorTipoDeEntrega
from controladores.controlador_encomenda import ControladorEncomenda

import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__database = psycopg2.connect(os.getenv("DB_CONNECTION_STRING"))
        self.__database.autocommit = True
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_tipo_de_entrega = ControladorTipoDeEntrega(self)
        self.__controlador_encomenda = ControladorEncomenda(self)

    @property
    def database(self):
        return self.__database
    
    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega
    
    @property
    def controlador_encomenda(self):
        return self.__controlador_encomenda

    def inicializa_sistema(self):
        # if not self.login():
        #     return

        self.abre_tela()

    def abre_tela(self):
        self.__tela_sistema.abre_tela()

    def login(self):
        return self.__controlador_funcionario.abre_tela_login()

    def menu_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega.abre_tela()
    
    def menu_encomenda(self):
        return self.__controlador_encomenda.abre_tela_encomenda()
    
    def encerra_sistema(self):
        self.__database.close()
        exit()

    def abre_tela(self):
        lista_opcoes = {
            1: self.menu_tipo_de_entrega,
            2: self.menu_encomenda,
            0: self.encerra_sistema,
        }

        while True:
            opcao = self.__tela_sistema.abre_tela()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()