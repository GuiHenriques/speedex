from telas.tela_tipo_de_entrega import TelaTiposDeEntrega
from entidades.tipo_de_entrega import tipoDeEntrega


from psycopg2 import extensions


class ControladorTipoDeEntrega:
    def __init__(self, controlador_sistema):
        self.__tela_tipo_de_entrega = TelaTiposDeEntrega(self)
        self.__controlador_sistema = controlador_sistema
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_tipo_de_entrega,
            2: self.alterar_tipo_de_entrega,
            3: self.excluir_tipo_de_entrega,
            4: self.listar_tipo_de_entrega,
            0: "Retornar para menu principal",
        }

        while True:
            opcao = self.__tela_tipo_de_entrega.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()

    def pegar_tipo_de_entrega_por_id(self, id):
        self.__cursor.execute("SELECT * FROM tipos_de_entrega WHERE id = %s", (id,))
        tipo_de_entrega = self.__cursor.fetchone()
        if tipo_de_entrega:
            return tipo_de_entrega
        else:
            self.__tela_tipo_de_entrega.mensagem("Tipo de entrega não encontrado para o ID fornecido.")
            return None
    
    def incluir_tipo_de_entrega(self):
        dados_tipo_de_entrega = self.__tela_tipo_de_entrega.pega_dados_tipo_de_entrega()
        if dados_tipo_de_entrega == None:
            return
        

        consulta_max_id = "SELECT MAX(id) FROM tipos_de_entrega"
        self.__cursor.execute(consulta_max_id)
        max_id = self.__cursor.fetchone()[0]
        novo_id = max_id + 1 if max_id is not None else 1

        

        self.__cursor.execute("INSERT INTO tipos_de_entrega (id, nome, taxa, descricao) VALUES (%s, %s, %s, %s)",
                              (novo_id, dados_tipo_de_entrega["nome"], dados_tipo_de_entrega["taxa"], dados_tipo_de_entrega["descricao"]))

        self.__controlador_sistema.database.commit()
        self.__tela_tipo_de_entrega.mensagem("Tipo de entrega cadastrado com sucesso.")
        return True

    def alterar_tipo_de_entrega(self):
        codigo_selecionado = self.__tela_tipo_de_entrega.seleciona_codigo_tipo_de_entrega()
        tipo_de_entrega = self.pegar_tipo_de_entrega_por_id(codigo_selecionado)
        if tipo_de_entrega is not None:
            dados_tipo_de_entrega = self.__tela_tipo_de_entrega.pega_dados_tipo_de_entrega()
            if dados_tipo_de_entrega == None:
                return False
            
            self.__cursor.execute("UPDATE tipos_de_entrega SET nome = %s, taxa = %s, descricao = %s WHERE id = %s",
                                  (dados_tipo_de_entrega["nome"], dados_tipo_de_entrega["taxa"], dados_tipo_de_entrega["descricao"], codigo_selecionado))
            self.__controlador_sistema.database.commit()

            self.__tela_tipo_de_entrega.mensagem("Tipo de entrega alterado com sucesso!")
            return True

    def excluir_tipo_de_entrega(self):
        codigo_selecionado = self.__tela_tipo_de_entrega.seleciona_codigo_tipo_de_entrega()
        tipo_de_entrega = self.pegar_tipo_de_entrega_por_id(codigo_selecionado)
        if tipo_de_entrega is not None:
            self.__cursor.execute("DELETE FROM tipos_de_entrega WHERE id = %s", (codigo_selecionado,))
            self.__controlador_sistema.database.commit()
            self.__tela_tipo_de_entrega.mensagem("Tipo de entrega excluído com sucesso!")

    def listar_tipo_de_entrega(self):
        self.__cursor.execute("SELECT * FROM tipos_de_entrega")
        resultados = self.__cursor.fetchall()
        
        self.__tela_tipo_de_entrega.mostra_tipo_de_entrega(resultados)