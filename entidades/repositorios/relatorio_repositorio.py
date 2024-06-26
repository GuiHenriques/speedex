from psycopg2 import extensions


class RelatorioRepositorio:
    def __init__(self, controlador_sistema) -> None:
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def pega_entregas_por_cpf(self, cpf) -> list:
        try:
            header = (
                "ID",
                "CPF Remet.",
                "Remetente",
                "CPF Destinat.",
                "Destinatario",
                "CPF Func.",
                "Funcionario",
                "Altura",
                "Largura",
                "Comprim.",
                "Tipo de Cx",
                "Conteudo",
                "Taxa Cx",
                "Tipo Entrega",
                "Taxa E.",
                "CEP",
                "Data",
                "Distancia",
                "Valor",
            )

            self.__cursor.execute(
                f"SELECT et.id, et.remetente_cpf, et.remetente_nome, et.destinatario_cpf, et.destinatario_nome, et.funcionario_cpf, et.funcionario_nome, \
                    ec.tipo_de_caixa_altura, ec.tipo_de_caixa_largura, ec.tipo_de_caixa_comprimento, ec.tipo_de_caixa_nome, ec.conteudo, ec.tipo_de_caixa_taxa, \
                    et.tipo_de_entrega_nome, et.tipo_de_entrega_taxa, c.cep, et.created_at, et.distancia, et.valor \
                    FROM entregas et JOIN encomendas ec ON et.encomenda_id = ec.id JOIN clientes c ON et.destinatario_cpf = c.cpf \
                    WHERE remetente_cpf='{cpf}' OR destinatario_cpf='{cpf}';"
            )
            entregas = self.__cursor.fetchall()
            return entregas
        except Exception as e:
            print(e)
            return None

    def pega_entrega_por_periodo(self, inicio, fim) -> list:
        try:
            self.__cursor.execute(
                f"SELECT et.id, et.remetente_cpf, et.remetente_nome, et.destinatario_cpf, et.destinatario_nome, et.funcionario_cpf, et.funcionario_nome, \
                    ec.tipo_de_caixa_altura, ec.tipo_de_caixa_largura, ec.tipo_de_caixa_comprimento, ec.tipo_de_caixa_nome, ec.conteudo, ec.tipo_de_caixa_taxa, \
                    et.tipo_de_entrega_nome, et.tipo_de_entrega_taxa, c.cep, et.created_at, et.distancia, et.valor \
                    FROM entregas et JOIN encomendas ec ON et.encomenda_id = ec.id JOIN clientes c ON et.destinatario_cpf = c.cpf \
                    WHERE created_at BETWEEN '{inicio}' AND '{fim}';"
            )
            entregas = self.__cursor.fetchall()
            return entregas
        except Exception as e:
            print(e)
            return None

    def relatorio_tipo_de_entrega(self, inicio, fim):
        try:
            self.__cursor.execute(
                f"SELECT tipo_de_entrega_id, tipo_de_entrega_nome, tipo_de_entrega_taxa, COUNT(*) \
                    FROM entregas GROUP BY tipo_de_entrega_id, tipo_de_entrega_nome, tipo_de_entrega_taxa \
                    ORDER BY COUNT(*) DESC;"
            )
            tipos_de_entrega_filtrados = self.__cursor.fetchall()
            return tipos_de_entrega_filtrados
        except Exception as e:
            print(e)
            return None

    def relatorio_tipo_de_caixa(self): ...
