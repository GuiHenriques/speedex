from telas.tela_cliente import TelaCliente


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema