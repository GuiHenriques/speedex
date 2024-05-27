from entidades.modelos.entrega import Entrega

from psycopg2 import extensions


class EntregaRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_entrega(self, entrega: Entrega):

        try:
            self.__cursor.execute(
                f"INSERT INTO entregas(remetente_cpf, destinatario_cpf, encomenda_id, tipo_de_entrega_id, funcionario_cpf, distancia) \
                    VALUES ({entrega.remetente.cpf}, {entrega.destinatario.cpf}, {entrega.encomenda.id}, {entrega.tipo_de_entrega.id},\
                            {entrega.funcionario.cpf}, {entrega.distancia});"
            )

        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."

        return True, ""

    def registrar_encomenda(self, encomenda):
        if encomenda.tipo_de_caixa.id is None:
            encomenda.tipo_de_caixa = "NULL"
        else:
            encomenda.tipo_de_caixa = encomenda.tipo_de_caixa.id
        try:
            self.__cursor.execute(
                f"INSERT INTO encomendas(conteudo, peso, tipo_de_caixa_id) \
                  VALUES ('{encomenda.conteudo}', {encomenda.peso}, {encomenda.tipo_de_caixa});"
            )
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."

        return True, ""

    def pegar_id_ultima_encomenda(self):
        try:
            self.__cursor.execute("SELECT MAX(id) FROM encomendas;")
            return self.__cursor.fetchone()[0]
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
