from telas.tela_cliente import TelaCliente
from entidades.repositorios.cliente_repositorio import ClienteRepositorio
from entidades.modelos.remetente import Remetente
from entidades.modelos.destinatario import Destinatario
from entidades.modelos.endereco import Endereco

from utils.valildadores import cpf_validador

import urllib.request
import json


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__tela = TelaCliente() if not controlador_sistema.development_mode else None
        self.__controlador_sistema = controlador_sistema
        self.__repositorio = ClienteRepositorio(controlador_sistema)
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.menu_cadastro_de_cliente,
            2: self.menu_alterar_cliente,
            3: self.menu_excluir_cliente,
            4: self.listar_clientes,
            0: "Retornar para o menu principal",
        }

        while True:
            opcao = self.__tela.abre_tela()
            if opcao == 0:
                return

            opcao_escolhida = lista_opcoes[opcao]
            opcao_escolhida()

    def menu_cadastro_de_cliente(self):
        while True:
            evento, valores = self.__tela.pega_dados_de_cliente()
            
            if evento == None:
                return

            if evento == "Confirmar" and valores == None:
                continue

            cpf = valores["cpf"]
            nome = valores["nome"]
            
            if valores["cep"] != "" or valores["estado"] != "":
                endereco = Endereco(
                    valores["cep"],
                    valores["estado"],
                    valores["cidade"],
                    valores["bairro"],
                    valores["rua"],
                    valores["numero"],
                )
            else:
                endereco = None

            if self.cadastrar_cliente(cpf, nome, endereco):
                return

    def cadastrar_cliente(self, cpf: str, nome: str, endereco: Endereco = None) -> bool:
        if not cpf_validador(cpf):
            self.__mensagem("CPF inválido!")
            return False

        cliente = None
        if endereco is None:
            cliente = Remetente(cpf, nome)
        else:
            cliente = Destinatario(cpf, nome, endereco)
        
        if self.cpf_existe(cliente.cpf):
            self.__mensagem("CPF já cadastrado!")
            return False
        
        if isinstance(cliente, Destinatario):
            if not self.__cep_existe(cliente.endereco.cep):
                self.__mensagem("CEP Inválido!")
                return False

        cliente_foi_cadastrado, msg_error = self.__repositorio.registrar_cliente(cliente)
        if cliente_foi_cadastrado:
            self.__mensagem("Cliente cadastrado com sucesso!")
            return cliente
        else:
            self.__mensagem(f"Não foi possível cadastrar o cliente.\n{msg_error}")
            return False
        
    def menu_excluir_cliente(self):
        while True:
            evento, valores = self.__tela.pega_cpf_cliente()

            if evento == None:
                return
            
            if evento == "Confirmar" and valores == None:
                continue
            
            cpf = valores["cpf"]
            if self.excluir_cliente(cpf):
                return
        
    def excluir_cliente(self, cpf: str):
        if not cpf_validador(cpf):
            self.__mensagem("CPF inválido!")
            return False

        if not self.cpf_existe(cpf):
            self.__mensagem("CPF não cadastrado!")
            return False

        cliente = self.__repositorio.pega_cliente(cpf)
        cliente_foi_excluido, msg_error = self.__repositorio.excluir_cliente(cliente)
        if cliente_foi_excluido:
            self.__mensagem(f"Cliente {cliente.cpf}, {cliente.nome} excluído!")
            return cliente
        else:
            self.__mensagem(f"Não foi possível excluir o cliente.\n{msg_error}")
            return False

    def menu_alterar_cliente(self):
        while True:
            evento, valores = self.__tela.pega_cpf_cliente()

            if evento == None:
                return
            
            if evento == "Confirmar" and valores == None:
                continue

            cpf = valores["cpf"]

            if not cpf_validador(cpf):
                self.__mensagem("CPF inválido!")
                continue

            if not self.cpf_existe(cpf):
                self.__mensagem("CPF não cadastrado!")
                continue

            cliente = self.__repositorio.pega_cliente(cpf)
            
            while True:
                if isinstance(cliente, Destinatario):
                    evento, valores = self.__tela.pega_dados_de_cliente(
                        cliente.nome, cliente.endereco.cep, cliente.endereco.estado,
                        cliente.endereco.cidade, cliente.endereco.bairro, cliente.endereco.rua, cliente.endereco.numero
                    )
                else:
                    evento, valores = self.__tela.pega_dados_de_cliente(
                        cliente.nome
                    )

                if evento == None:
                    break
                
                if evento == "Confirmar" and valores == None:
                    continue

                break

            if valores == None:
                continue

            nome = valores["nome"]

            if valores["cep"] != "" or valores["estado"] != "":
                endereco = Endereco(
                    valores["cep"],
                    valores["estado"],
                    valores["cidade"],
                    valores["bairro"],
                    valores["rua"],
                    valores["numero"],
                )
            else:
                endereco = None

            if self.alterar_cliente(cpf, nome, endereco):
                return

    def alterar_cliente(self, cpf: str, nome: str, endereco: Endereco = None):
        if endereco is None:
            cliente = Remetente(cpf, nome)
        else:
            cliente = Destinatario(cpf, nome, endereco)

        if isinstance(cliente, Destinatario):
            if not self.__cep_existe(cliente.endereco.cep):
                self.__mensagem("CEP Inválido!")
                return False

        cliente_foi_atualizado, msg_error = self.__repositorio.atualizar_dados_de_cliente(cliente)
        if cliente_foi_atualizado:
            self.__mensagem("Cliente atualizado com sucesso!")
            return cliente
        else:
            self.__mensagem(f"Não foi possível atualizar os dados do cliente.\n{msg_error}")
            return False
        
    def listar_clientes(self):
        clientes = self.__repositorio.pega_todos_os_clientes()
        if clientes:
            self.__tela.mostra_cliente(clientes)
        else:
            self.__mensagem("Nenhum cliente cadastrado!")

    def pega_cliente_por_cpf(self, cpf: str):
        cliente = self.__repositorio.pega_cliente(cpf)
        return cliente

    def cpf_existe(self, cpf: str):
        if self.__repositorio.pega_cliente(cpf) == None:
            return False
        else:
            return True
        
    def __cep_existe(self, cep: str):
        url = f'https://viacep.com.br/ws/{cep}/json'
        headers = { 'User-Agent': 'Autociencia/1.0' }
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        client = urllib.request.urlopen(req)
        content = client.read().decode('utf-8')
        address = json.loads(content)
        client.close()

        return "cep" in address

    def __mensagem(self, msg):
        try:
            self.__tela.mensagem(msg)
        except AttributeError:
            pass