from telas.tela_encomenda import TelaEncomenda
from utils.valildadores import campo_vazio_validador
from entidades.repositorios.encomenda_repositorio import EncomendaRepositorio

class ControladorEncomenda:
    def __init__(self, controlador_sistema):
        self.__tela_encomenda = TelaEncomenda()
        self.__repositorio_encomenda = EncomendaRepositorio(controlador_sistema)

    @property
    def tela_encomenda(self):
        return self.__tela_encomenda
    
    def abre_tela_encomenda(self):
        while True:
            
            valores_encomenda = self.tela_encomenda.tela_encomenda()

            if valores_encomenda == None:
                return False
            
            if campo_vazio_validador(valores_encomenda):
                self.tela_encomenda.mensagem("Erro", "Por favor, preencha todos os campos.")
                continue

            # verificar se o cpf do remetente e do destinatario existem no banco de dados

            # verificar se o cpf do remetente e do destinatario são iguais

            # se usuario tem caixa
            if valores_encomenda["caixa_sim"] == True:
                valores_caixa = self.tela_encomenda.tela_possui_caixa()

                if valores_caixa == None:
                    return False
                
                # registrar encomenda
                print("Encomenda registrada com sucesso!")
                break
            else:
                valores_caixa = self.tela_encomenda.tela_nao_possui_caixa()

                if valores_caixa == None:
                    return False
                
                # registrar encomenda
                print("Encomenda registrada com sucesso!")
                break


