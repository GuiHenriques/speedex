from entidades.modelos.tipo_de_caixa import TipoDeCaixa

from psycopg2 import extensions

class tipoDeCaixaRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_tipo_de_caixa(self, tipodecaixa: TipoDeCaixa):
        try:
<<<<<<< HEAD
            self.__cursor.execute(f"INSERT INTO tipo_de_caixa(id, nome, taxa, altura, largura, comprimento) \
                                VALUES ('{tipodecaixa.id}', '{tipodecaixa.nome}', '{tipodecaixa.taxa}', '{tipodecaixa.dimensoes.altura}', '{tipodecaixa.dimensoes.largura}','{tipodecaixa.dimensoes.comprimento}');")
=======
            self.__cursor.execute(f"INSERT INTO tipos_de_caixa(id, nome, taxa, dimensoes) \
                                VALUES ('{tipodecaixa.id}', '{tipodecaixa.nome}', '{tipodecaixa.taxa}', '{tipodecaixa.dimensoes}');")
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    def pegar_tipo_de_caixa_por_id(self, id):
        dados_tipo_de_caixa: tuple = None
        try:
<<<<<<< HEAD
            self.__cursor.execute(f"SELECT * FROM tipo_de_caixa\
=======
            self.__cursor.execute(f"SELECT * FROM tipos_de_caixa\
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
                                  WHERE id='{id}'")
            dados_tipo_de_caixa = self.__cursor.fetchone()
        except Exception as e:
            self.__tela.mensagem("Tipo de caixa não encontrado para o ID fornecido.")
        
        if dados_tipo_de_caixa != None:
            tipodecaixa = TipoDeCaixa(*dados_tipo_de_caixa)
            return tipodecaixa