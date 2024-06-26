from entidades.modelos.entrega import Entrega
from entidades.modelos.encomenda import Encomenda

from psycopg2 import extensions


class EntregaRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_entrega(self, entrega: Entrega):
        try:
            self.__cursor.execute(
                f"INSERT INTO entregas(remetente_cpf, remetente_nome, destinatario_cpf, destinatario_nome, \
                    funcionario_cpf, funcionario_nome, encomenda_id, tipo_de_entrega_id, tipo_de_entrega_nome,\
                    tipo_de_entrega_taxa, distancia, valor)\
                    VALUES ('{entrega.remetente.cpf}', '{entrega.remetente.nome}', '{entrega.destinatario.cpf}', '{entrega.destinatario.nome}', \
                    '{entrega.funcionario.cpf}', '{entrega.funcionario.nome}', {entrega.encomenda.id}, {entrega.tipo_de_entrega.id}, \
                    '{entrega.tipo_de_entrega.nome}', {entrega.tipo_de_entrega.taxa}, {entrega.distancia}, {entrega.valor});"
            )

        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."

        return True, ""

    def registrar_encomenda(self, encomenda: Encomenda):
        if encomenda.tipo_de_caixa.id is None:
            encomenda.tipo_de_caixa.id = "NULL"
            encomenda.tipo_de_caixa.taxa = 0

        try:
            self.__cursor.execute(
                f"INSERT INTO encomendas(conteudo, peso, tipo_de_caixa_id, tipo_de_caixa_nome,\
                    tipo_de_caixa_taxa, tipo_de_caixa_altura, tipo_de_caixa_largura, tipo_de_caixa_comprimento) \
                    VALUES ('{encomenda.conteudo}', {encomenda.peso}, {encomenda.tipo_de_caixa.id},\
                    '{encomenda.tipo_de_caixa.nome}', {encomenda.tipo_de_caixa.taxa}, {encomenda.tipo_de_caixa.dimensoes.altura},\
                     {encomenda.tipo_de_caixa.dimensoes.largura}, {encomenda.tipo_de_caixa.dimensoes.comprimento});"
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

    def tipos_de_entrega_mais_utilizados_por_periodo(self, inicio, fim):
        try:
            self.__cursor.execute(
                f"SELECT * FROM entregas \
                WHERE created_at BETWEEN '{inicio}' AND '{fim}';"
            )
            tipos_de_entrega_filtrados = self.__cursor.fetchall()
            return tipos_de_entrega_filtrados
        except Exception as e:
            print(e)
            return None
