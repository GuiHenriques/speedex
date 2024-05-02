from telas.tela_cliente import TelaCliente
from entidades.repositorios.cliente_repositorio import ClienteRepositorio


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__tela_cliente = TelaCliente() if not controlador_sistema.development_mode else None
        self.__controlador_sistema = controlador_sistema
        self.__repositorio = ClienteRepositorio(controlador_sistema)

    def abre_tela(self):
        while True:
            evento, valores = self.__tela_cliente.tela_cadastro()