from entidades.modelos.entrega import Entrega

from psycopg2 import extensions


class EntregaRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_entrega(self, entrega: Entrega):
        try:
            ...
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""