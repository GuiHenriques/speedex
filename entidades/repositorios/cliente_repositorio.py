from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario
from entidades.modelos.endereco import Endereco
from utils.formatadores import cpf_formatador

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
    
    def excluir_cliente(self, cliente: Remetente | Destinatario) -> bool:
        try:
            self.__cursor.execute(f"DELETE FROM clientes WHERE cpf='{cliente.cpf}';")
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    def pega_cliente(self, cpf: str):
        cpf = cpf_formatador(cpf)
        dados_cliente: tuple = None
        try:
            self.__cursor.execute(f"SELECT * FROM clientes WHERE cpf='{cpf}';")
            dados_cliente = self.__cursor.fetchone()
        except Exception as e:
            print(e)
            return None
        
        if dados_cliente != None:
            cpf = dados_cliente[0]
            nome = dados_cliente[1]
            if None in dados_cliente:
                return Remetente(cpf, nome)
            else:
                endereco = Endereco(*dados_cliente[2:])
                return Destinatario(cpf, nome, endereco)
    
    def excluir_cliente(self, cliente: Remetente | Destinatario) -> bool:
        try:
            self.__cursor.execute(f"DELETE FROM clientes WHERE cpf='{cliente.cpf}';")
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    def pega_cliente(self, cpf: str):
        cpf = cpf_formatador(cpf)
        dados_cliente: tuple = None
        try:
            self.__cursor.execute(f"SELECT * FROM clientes WHERE cpf='{cpf}';")
            dados_cliente = self.__cursor.fetchone()
        except Exception as e:
            print(e)
            return None
        
        if dados_cliente != None:
            cpf = dados_cliente[0]
            nome = dados_cliente[1]
            if None in dados_cliente:
                return Remetente(cpf, nome)
            else:
                endereco = Endereco(*dados_cliente[2:])
                return Destinatario(cpf, nome, endereco)
        
    def excluir_cliente(self, cliente: Remetente | Destinatario) -> bool:
        try:
            self.__cursor.execute(f"DELETE FROM clientes WHERE cpf='{cliente.cpf}';")
        except Exception as e:
            print(e)
            return False, "Erro interno no banco de dados."
        
        return True, ""
    
    def atualizar_dados_de_cliente(self, cliente: Remetente | Destinatario) -> tuple[bool, str]:
        if isinstance(cliente, Remetente):
            try:
                self.__cursor.execute(f"UPDATE clientes SET nome='{cliente.nome}', cep='',\
                                      estado='', cidade='', bairro='', rua='', numero=''\
                                      WHERE cpf='{cliente.cpf}';")
            except Exception as e:
                print(e)
                return False, "Erro interno no banco de dados."
        else:
            try:
                self.__cursor.execute(f"UPDATE clientes SET nome='{cliente.nome}', cep='{cliente.endereco.cep}',\
                                      estado='{cliente.endereco.estado}', cidade='{cliente.endereco.cidade}',\
                                      bairro='{cliente.endereco.bairro}', rua='{cliente.endereco.rua}',\
                                      numero='{cliente.endereco.numero}'\
                                      WHERE cpf='{cliente.cpf}';")
            except Exception as e:
                print(e)
                return False, "Erro interno no banco de dados."
            
        return True, ""
        
    
    def pega_todos_os_clientes(self):
        try:
            self.__cursor.execute(f"SELECT * FROM clientes;")
            rows = self.__cursor.fetchall()
        except Exception as e:
            print(e)
            return None

        if rows is None:
            return None

        clientes = [[field if field is not None else '' for field in row] for row in rows]        
        return clientes

    def pega_cliente(self, cpf: str):
        cpf = cpf_formatador(cpf)
        dados_cliente: tuple = None
        try:
            self.__cursor.execute(f"SELECT * FROM clientes WHERE cpf='{cpf}';")
            dados_cliente = self.__cursor.fetchone()
        except Exception as e:
            print(e)
            return None
        
        if dados_cliente != None:
            cpf = dados_cliente[0]
            nome = dados_cliente[1]
            if None in dados_cliente:
                return Remetente(cpf, nome)
            else:
                endereco = Endereco(*dados_cliente[2:])
                return Destinatario(cpf, nome, endereco)