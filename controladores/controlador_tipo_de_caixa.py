from telas.tela_tipo_de_caixa import TelaTiposDeCaixa
from entidades.modelos.tipo_de_caixa import TipoDeCaixa
<<<<<<< HEAD
from entidades.modelos.caixa import Caixa
=======
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
from entidades.repositorios.tipo_de_caixa_repositorio import tipoDeCaixaRepositorio


from psycopg2 import extensions


class ControladorTipoDeCaixa:
    def __init__(self, controlador_sistema):
        self.__tela = TelaTiposDeCaixa(self)
        self.__controlador_sistema = controlador_sistema
        self.__cursor: extensions.cursor = controlador_sistema.database.cursor()
        self.__repositorio = tipoDeCaixaRepositorio(controlador_sistema)


    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_tipo_de_caixa,
            2: self.alterar_tipo_de_caixa,
            3: self.excluir_tipo_de_caixa,
            4: self.listar_tipo_de_caixa,
            0: "Retornar para menu principal",
        }

        while True:
            opcao = self.__tela.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()

    def __mensagem(self, mensagem):
        try:
            self.__tela.mensagem(mensagem)
        except AttributeError as e: 
            pass

    def pegar_tipo_de_caixa_por_id(self, id):
<<<<<<< HEAD
        self.__cursor.execute("SELECT * FROM tipo_de_caixa WHERE id = %s", (id,))
=======
        self.__cursor.execute("SELECT * FROM tipos_de_caixa WHERE id = %s", (id,))
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
        tipo_de_caixa = self.__cursor.fetchone()
        if tipo_de_caixa:
            return tipo_de_caixa
        else:
            self.__mensagem("Tipo de caixa não encontrado para o ID fornecido.")
            return None
    
    def incluir_tipo_de_caixa(self):
        dados_tipo_de_caixa = self.__tela.pega_dados_tipo_de_caixa()
        if dados_tipo_de_caixa == None:
            return
        

<<<<<<< HEAD
        consulta_max_id = "SELECT MAX(id) FROM tipo_de_caixa"
=======
        consulta_max_id = "SELECT MAX(id) FROM tipos_de_caixa"
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
        self.__cursor.execute(consulta_max_id)
        max_id = self.__cursor.fetchone()[0]
        novo_id = max_id + 1 if max_id is not None else 1

<<<<<<< HEAD
        nova_caixa = Caixa(dados_tipo_de_caixa["altura"], dados_tipo_de_caixa["largura"], dados_tipo_de_caixa["comprimento"])
        novo_tipo_de_caixa = TipoDeCaixa(novo_id, dados_tipo_de_caixa["nome"], dados_tipo_de_caixa["taxa"], nova_caixa)
=======
        
        novo_tipo_de_caixa = TipoDeCaixa(novo_id, dados_tipo_de_caixa["nome"], dados_tipo_de_caixa["taxa"], dados_tipo_de_caixa["dimensoes"])
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb

        cadastrado, msg_error = self.__repositorio.registrar_tipo_de_caixa(novo_tipo_de_caixa)
        if cadastrado:
            self.__mensagem("Tipo de caixa cadastrado com sucesso.")
            return novo_tipo_de_caixa
        else:
            self.__mensagem(f"Não foi possível cadastrar o tipo de caixa:\n{msg_error}")
            return False


    def alterar_tipo_de_caixa(self):
        codigo_selecionado = self.__tela.seleciona_codigo_tipo_de_caixa()
        tipo_de_caixa = self.pegar_tipo_de_caixa_por_id(codigo_selecionado)
        if tipo_de_caixa is not None:
            dados_tipo_de_caixa = self.__tela.pega_dados_tipo_de_caixa()
            if dados_tipo_de_caixa == None:
                return False
            
<<<<<<< HEAD
            self.__cursor.execute("UPDATE tipo_de_caixa SET nome = %s, taxa = %s, altura = %s, largura = %s, comprimento = %s WHERE id = %s",
                                  (dados_tipo_de_caixa["nome"], dados_tipo_de_caixa["taxa"],dados_tipo_de_caixa["largura"],dados_tipo_de_caixa["altura"],dados_tipo_de_caixa["comprimento"], codigo_selecionado))
=======
            self.__cursor.execute("UPDATE tipos_de_caixa SET nome = %s, taxa = %s, descricao = %s WHERE id = %s",
                                  (dados_tipo_de_caixa["nome"], dados_tipo_de_caixa["taxa"], dados_tipo_de_caixa["dimensoes"], codigo_selecionado))
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
            self.__controlador_sistema.database.commit()

            self.__mensagem("Tipo de caixa alterado com sucesso!")
            return True

    def excluir_tipo_de_caixa(self):
        codigo_selecionado = self.__tela.seleciona_codigo_tipo_de_caixa()
        tipo_de_caixa = self.pegar_tipo_de_caixa_por_id(codigo_selecionado)
        if tipo_de_caixa is not None:
<<<<<<< HEAD
            self.__cursor.execute("DELETE FROM tipo_de_caixa WHERE id = %s", (codigo_selecionado,))
=======
            self.__cursor.execute("DELETE FROM tipos_de_caixa WHERE id = %s", (codigo_selecionado,))
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
            self.__controlador_sistema.database.commit()
            self.__mensagem("Tipo de caixa excluído com sucesso!")

    def listar_tipo_de_caixa(self):
<<<<<<< HEAD
        self.__cursor.execute("SELECT * FROM tipo_de_caixa")
=======
        self.__cursor.execute("SELECT * FROM tipos_de_caixa")
>>>>>>> 59ddabe3ca3a8fa7195d831ea3eaabed8bf07cbb
        resultados = self.__cursor.fetchall()
        
        self.__tela.mostra_tipo_de_caixa(resultados)