from telas.tela_sistema import TelaSistema
from controladores.controlador_login import ControladorLogin
from controladores.controlador_tipo_de_entrega import ControladorTipoDeEntrega

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_login = ControladorLogin()
        self.__controlador_tipo_de_entrega = ControladorTipoDeEntrega()

    @property
    def controlador_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega

    def inicializa_sistema(self):
        # if not self.login():
        #     return

        self.abre_tela()



    def abre_tela(self):
        self.__tela_sistema.abre_tela()

    def login(self):
        return self.__controlador_login.abre_tela()

    def menu_tipo_de_entrega(self):
        return self.__controlador_tipo_de_entrega.abre_tela()
    
    def encerra_sistema(self):
        exit()

    def abre_tela(self):
        lista_opcoes = {
            1: self.menu_tipo_de_entrega, 
            0: self.encerra_sistema,
        }

        while True:
            opcao = self.__tela_sistema.abre_tela()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()