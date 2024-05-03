from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario

from psycopg2 import extensions


class ClienteRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor = extensions.cursor = controlador_sistema.database.cursor()

    def registrar_cliente(self, cliente: Remetente | Destinatario):
        if isinstance(cliente, Remetente):
            ...
        else:
            ...

        return True, ""