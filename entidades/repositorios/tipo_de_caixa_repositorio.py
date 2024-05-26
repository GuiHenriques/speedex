from entidades.modelos.tipo_de_caixa import TipoDeCaixa
from telas.tela_tipo_de_caixa import TelaTiposDeCaixa
from psycopg2 import extensions

class tipoDeCaixaRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()
        self.__tela = TelaTiposDeCaixa(self)


    def registrar_tipo_de_caixa(self, tipodecaixa: TipoDeCaixa):
        try:
            self.__cursor.execute(f"INSERT INTO tipo_de_caixa( nome, taxa, altura, largura, comprimento) \
                                VALUES ( '{tipodecaixa.nome}', '{tipodecaixa.taxa}', '{tipodecaixa.dimensoes.altura}', '{tipodecaixa.dimensoes.largura}','{tipodecaixa.dimensoes.comprimento}');")
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    def pegar_tipo_de_caixa_por_id(self, id):
        self.__cursor.execute("SELECT * FROM tipo_de_caixa WHERE id = %s", (id,))
        tipo_de_caixa = self.__cursor.fetchone()
        if tipo_de_caixa:
            return tipo_de_caixa
        else:
            self.__tela.mensagem("Tipo de caixa não encontrado para o ID fornecido.")
            return None
        

































        # dados_tipo_de_caixa: tuple = None
        # try:
        #     self.__cursor.execute(f"SELECT * FROM tipo_de_caixa\
        #                           WHERE id='{id}'")
        #     dados_tipo_de_caixa = self.__cursor.fetchone()
        # except Exception as e:
        #     # self.__tela.mensagem("Tipo de caixa não encontrado para o ID fornecido.")
        #     print(e)
        # if dados_tipo_de_caixa != None:
        #     tipodecaixa = TipoDeCaixa(*dados_tipo_de_caixa)
        #     return tipodecaixa