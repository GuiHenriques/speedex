from entidades.modelos.encomenda import Encomenda

from psycopg2 import extensions

class EncomendaRepositorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_encomenda(self, encomenda: Encomenda):
        try:
            self.__cursor.execute(f"INSERT INTO encomendas(conteudo, tipo_de_caixa) VALUES ('{encomenda.conteudo}', '{encomenda.tipo_de_caixa}');")
            self.__controlador_sistema.database.commit()
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, None
    
    def pegar_encomenda(self, id_encomenda):
        dados_encomenda: tuple = None
        try:
            self.__cursor.execute(f"SELECT * FROM encomendas WHERE id_encomenda={id_encomenda}")
            dados_encomenda = self.__cursor.fetchone()
        except Exception as e:
            print(e)
        
        if dados_encomenda != None:
            encomenda = Encomenda(*dados_encomenda)
            return encomenda