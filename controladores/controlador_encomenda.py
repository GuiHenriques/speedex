from telas.tela_encomenda import TelaEncomenda
from utils.valildadores import campo_vazio_validador, campo_numerico_validador
from entidades.repositorios.encomenda_repositorio import EncomendaRepositorio

# from entidades.repositorios.cliente_repositorio import ClienteRepositorio


class ControladorEncomenda:
    def __init__(self, controlador_sistema):
        self.__tela = TelaEncomenda() if not controlador_sistema.development_mode else None
        self.__repositorio = EncomendaRepositorio(controlador_sistema)
        # self.__repositorio_cliente = ClienteRepositorio(controlador_sistema)

    @property
    def tela(self):
        return self.__tela

    def abre_tela_encomenda(self):
        while True:
            evento, valores_encomenda = self.__tela.tela_encomenda()

            if evento == None or evento == "voltar":
                return False

            if not self.__verificar_campos_validos_encomenda(valores_encomenda):
                continue
            
            # se usuario tem caixa
            if valores_encomenda["caixa_sim"]:
                valores_caixa = self.tela_encomenda.tela_possui_caixa()
                # valores_caixa = {"altura": "10", "largura": "10", "comprimento": "10"}
                if valores_caixa == None:
                    return False

                # validação dos campos
                if not self.__verificar_campos_validos_caixa(valores_caixa):
                    continue

            else:
                valores_caixa = self.tela_encomenda.tela_nao_possui_caixa()
                # pegar dimensões da caixa selecionada
                
                if valores_caixa == None:
                    return False

            # registrar encomenda
            valores = {**valores_encomenda, **valores_caixa}
            print(valores)
            self.processar_encomenda(valores)
            break

    def registrar_encomenda(self, valores):

        # registrar encomenda no banco de dados
        # self.__repositorio.registrar_encomenda()

        self.__tela.tela_cadastrada()

    def __verificar_campos_validos_encomenda(self, valores_encomenda):

        # verificar se todos os campos foram preenchidos
        if campo_vazio_validador(valores_encomenda):
            self.__mensagem("Por favor, preencha todos os campos.")
            return False

        # verificar se o cpf do remetente e do destinatario existem no banco de dados
        if not self.__verificar_cpf_existente(valores_encomenda["cpf_remetente"]):
            self.__mensagem("CPF do remetente não encontrado.")
            return False

        elif not self.__verificar_cpf_existente(valores_encomenda["cpf_destinatario"]):
            self.__mensagem("CPF do destinatário não encontrado.")
            return False

        # verificar se o cpf do remetente e do destinatario são iguais
        if valores_encomenda["cpf_remetente"] == valores_encomenda["cpf_destinatario"]:
            self.__mensagem("CPF do remetente e do destinatário são iguais.")
            return False
        
        # verificar se o peso é um número
        if not valores_encomenda["peso"].isnumeric():
            self.__mensagem("O peso deve ser um número inteiro positivo.")
            return False

        # verificar se a opção de entrega é valida
        # tipos_entrega = self.__repositorio_tipos_de_entrega.pegar_tipos_entrega()
        if valores_encomenda["opcao_entrega"] not in ["Expressa", "Normal", "Econômica"]:
            self.__mensagem("Opção de entrega inválida.")
            return False

        # ta puro
        return True

    def __verificar_campos_validos_caixa(self, valores_caixa):
        
        # verificar se todos os campos foram preenchidos
        if campo_vazio_validador(valores_caixa):
            self.__mensagem("Por favor, preencha todos os campos.")
            return False

        # verificar se a altura, largura e comprimento são números
        if not campo_numerico_validador(valores_caixa):
            self.__mensagem("As dimensões da caixa devem ser números inteiros positivos.")
            return False

        return True

    def __verificar_cpf_existente(self, cpf: str):
        # if self.__repositorio_cliente.pegar_funcionario(cpf) == None:
        #     return False
        return True

    def __mensagem(self, msg: str):
        try:
            self.__tela.mensagem(msg)
        except AttributeError:
            pass