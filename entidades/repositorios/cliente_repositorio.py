from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario

from psycopg2 import extensions


class ClienteRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_cliente(self, cliente: Remetente | Destinatario):
        if isinstance(cliente, Destinatario):
            try:
                self.__cursor.execute(f"INSERT INTO clientes(cpf, nome, cep, estado, cidade, bairro, rua, numero) \
                                        VALUES ('{cliente.cpf}', '{cliente.nome}', '{cliente.endereco.cep}', \
                                                '{cliente.endereco.estado}', '{cliente.endereco.cidade}', '{cliente.endereco.bairro}', \
                                                '{cliente.endereco.rua}', '{cliente.endereco.numero}');")
            except Exception as e:
                print(e)
                return False, "Erro interno no banco de dados."
        else:
            try:
                self.__cursor.execute(f"INSERT INTO clientes(cpf, nome) VALUES ('{cliente.cpf}', '{cliente.nome}');")
            except Exception as e:
                print(e)
                return False, "Erro interno no banco de dados."

        return True, ""