from psycopg2 import extensions


class RelatorioRepositorio:
    def __init__(self, controlador_sistema) -> None:
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def pega_entregas_por_cpf(self, cpf) -> list:
        try:
            self.__cursor.execute(f"SELECT * FROM entregas \
                                    WHERE remetente_cpf='{cpf}' \
                                    OR destinatario_cpf='{cpf}';")
            entregas = self.__cursor.fetchall()
            return entregas
        except Exception as e:
            print(e)
            return None
    
    def pega_entrega_por_periodo(self, inicio, fim) -> list:
        try:
            self.__cursor.execute(f"SELECT * FROM entregas \
                                    WHERE created_at \
                                    BETWEEN '{inicio}' AND '{fim}';") 
            entregas = self.__cursor.fetchall()
            return entregas
        except Exception as e:
            print(e)
            return None

    def relatorio_tipo_de_entrega(self):
        ...

    def relatorio_tipo_de_caixa(self):
        ...