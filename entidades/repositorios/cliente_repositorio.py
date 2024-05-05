from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario

from psycopg2 import extensions


class ClienteRepositorio:
    def __init__(self, controlador_sistema):
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def registrar_cliente(self, cliente: Remetente | Destinatario):
        if isinstance(cliente, Remetente):
            try:
                self.__cursor.execute(f"INSERT INTO Clientes(cpf, nome, cep, estado, cidade, bairro, rua, numero)\
                                        VALUES ({cliente.cpf}, {cliente.nome}, {cliente.cep}, {cliente.estado}, {cliente.cidade}, {cliente.bairro}, {cliente.rua}, {cliente.numero});")
            except Exception as e:
                return False, "Erro interno no banco de dados."
        else:
            ...

        return True, ""