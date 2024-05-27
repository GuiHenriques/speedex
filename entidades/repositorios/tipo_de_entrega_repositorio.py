from entidades.modelos.tipo_de_entrega import tipoDeEntrega

from psycopg2 import extensions

class tipoDeEntregaRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_tipo_de_entrega(self, tipodeentrega: tipoDeEntrega):
        try:
            self.__cursor.execute(f"INSERT INTO tipos_de_entrega(id, nome, taxa, descricao, velocidade) \
                                VALUES ({tipodeentrega.id}, '{tipodeentrega.nome}', '{tipodeentrega.taxa}', '{tipodeentrega.descricao}', '{tipodeentrega.velocidade}');")
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    def pegar_tipo_de_entrega_por_id(self, id):
        dados_tipo_de_entrega: tuple = None
        try:
            self.__cursor.execute(f"SELECT * FROM tipos_de_entrega\
                                  WHERE id='{id}'")
            dados_tipo_de_entrega = self.__cursor.fetchone()
        except Exception as e:
            self.__tela.mensagem("Erro", "Tipo de entrega não encontrado para o ID fornecido.")
        
        if dados_tipo_de_entrega != None:
            tipodeentrega = tipoDeEntrega(*dados_tipo_de_entrega)
            return tipodeentrega
    
    def pegar_tipo_de_entrega_por_nome(self, nome):
        try:
            self.__cursor.execute(f"SELECT * FROM tipos_de_entrega WHERE nome='{nome}'")
            dados_tipo_de_entrega = self.__cursor.fetchone()
        
        except Exception as e:
            self.__tela.mensagem("Erro", "Tipo de entrega não encontrado para o nome fornecido.")
        
        if dados_tipo_de_entrega != None:
            tipodeentrega = tipoDeEntrega(*dados_tipo_de_entrega)
            return tipodeentrega

    def listar_nome_tipos_de_entrega(self):
        try:
            self.__cursor.execute("SELECT nome FROM tipos_de_entrega")
            tipos_de_entrega = self.__cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        
        return tipos_de_entrega
    
    def listar_tipos_de_entrega(self):
        try:
            self.__cursor.execute("SELECT * FROM tipos_de_entrega")
            tipos_de_entrega = self.__cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        
        return tipos_de_entrega