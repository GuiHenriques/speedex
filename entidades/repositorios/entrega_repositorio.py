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
    
    def pegar_tipos_de_caixa(self):
        tipos_de_caixa = []
        try:
            self.__cursor.execute("SELECT * FROM tipos_de_caixa")
            tipos_de_caixa = self.__cursor.fetchall()
        except Exception as e:
            self.__tela.mensagem("Erro ao buscar tipos de caixa.")

        return tipos_de_caixa
    