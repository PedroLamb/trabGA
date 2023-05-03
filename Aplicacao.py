from Figurinha import Figurinha
from Menu import *
import csv

class Aplicacao:
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.carregarFigurinhas()

    def executar(self):
        opcao = -1
        while not self.terminou:
            if self.tela == 0: #Tela inicial.
                self.TelaInicial()

            elif self.tela == 1: #Tela de gerenciamento do álbum.
                pass

            elif self.tela == 2: #Tela de gerenciamento da coleção do usuário.
                pass

    def finalizar(self):
        print('Finalizando a aplicação!')
        input('')
        #Salvar os dados nos arquivos e encerrar a aplicação.
        pass


    def carregarFigurinhas(self):
        pass #Implementar o carregamento dos arquivos csv das figurinhas.

    def msgErro(self, Codigo):
        pass #Implemenetar mensagem de erro.(Não entendi direto o exemplo da sora.)

    def telaInicial(self):
        opcao = menuInicial
        if opcao == '0':
            self.terminou == True
        else:
            pass #Chamar a função de erro aqui após ela ser implementada. 