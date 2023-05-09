from Usuario import Usuario
from Figurinha import Figurinha
from Album import *
from Menus import *
import csv


class Aplicacao:

    # Método construtor
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.carregarFigurinhas()

    def executar(self):
        opcao = -1
        while not self.terminou:
            if self.tela == 0: 
                self.telaInicial()      

            elif self.tela == 1:
                self.telaGerenciarAlbum()

            elif self.tela == 2: 
                self.telaGerenciarColecao()


    def finalizar(self):
        print('Finalizando a aplicacao!')
        # executar os salvamentos nos arquivos
        pass

    def criarUsuariosCSV(self):
        with open('Usuarios.csv', 'a') as criarusuarios: 
            pass 

    def carregarFigurinhas(self):
        # Abre o arquivo com as infos
        arqFigurinhas = open('FigurinhasDino.csv')
        # Faz a leitora do csv, agora com o delimitador certo
        leitor = csv.reader(arqFigurinhas,delimiter=';')
        # Transforma em lista 
        listaFig = list(leitor)
        # Nunca esqueça de fechar o arquivo!
        arqFigurinhas.close()

        # Aqui será a lista de todas as figurinhas que o album possui
        self.listaFigurinhas = []

        for i in range(len(listaFig)): #percorre linhas
            # Instancia um objeto da classe Figurinha, passando por parâmetro as colunas da tabela (já convertendo os nros para int)
            figurinha = Figurinha(int(listaFig[i][0]),listaFig[i][1],listaFig[i][2],int(listaFig[i][3]))                        
            # Adiciona na lista de figurinhas
            self.listaFigurinhas.append(figurinha)               

        # Manda imprimir o conteudo da lista de figurinhas -- apenas DEBUG, pode apagar depois
        for i in range(len(self.listaFigurinhas)):
            self.listaFigurinhas[i].imprimir()

    def msgErro(self, codigo):
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')

    # Processa as opções da Tela Inicial - 0
    def telaInicial(self):
        opcao = menuInicial()
        if opcao == '0':
            self.terminou = True
        elif opcao == '1':
            nome = input('Informe o nome de usuário que deseja utilizar: ')
            senha = input('Informe a senha que deseja utilizar: ')
            with open('Usuarios.csv', mode='r') as usuariosArq:
                reader = csv.reader(usuariosArq)
                for row in reader:
                    if row[0] == nome:
                        print("Nome de usuário já existe.")
                        input('Pressione ENTER para voltar à tela inicial...')
                        return
                else:
                    usuario = Usuario(nome, senha)
                    print('Cadastrando usuario....')
                    input('Pressione qualquer tecla para continuar...')
            usuario.cadastrarUsuario()
        elif opcao == '2':
            self.acessarAlbum()
        else:
            self.msgErro(1)
        

    # Processa as opções da Tela Gerenciar Album - 1
    def telaGerenciarAlbum(self):
        opcao = menuGerenciarAlbum()
        if opcao == '0':
            self.tela = 0  #muda para a tela inicial
        elif opcao == '1':
            verAlbum()
            input('Pressione ENTER para prosseguir...')
        elif opcao == '2':
            verColecao()
            input('Pressione ENTER para prosseguir...')
        elif opcao == '3':
            abrirPacote()
            input('Pressione ENTER para prosseguir...')
        else:
            self.msgErro(1)

     # Processa as opções da Tela Gerenciar Colecao - 2
    def telaGerenciarColecao(self):
        opcao = menuGerenciarColecao()
        if opcao == '0':
            self.tela = 1  #muda para a tela Gerenciar Album
        else:
            self.msgErro(1)

    def acessarAlbum(self):
        nome = input('Informe o seu nome de usuário: ')
        senha = input('Informe sua senha: ')
        usuario = Usuario(nome, senha)
        usuario.logarUsuario()
        if usuario.logarUsuario() == True:
            usuarioAtual.append(usuario.nome)
            with open(usuario.nome + ' - Album.csv', mode='r') as arqAlbuns:
                reader = csv.reader(arqAlbuns)
                for row in reader:
                        albumAtual.extend(row)
            with open(usuario.nome + ' - Colecao.csv', mode = 'r') as arqColecoes:
                reader = csv.reader(arqColecoes)
                for row in reader:
                        colecaoAtual.extend(row)
                print('Verificando usuario e recuperando o album do usuario')
                self.tela = 1
                input('Pressione qualquer tecla para continuar...')
        else:
            self.msgErro(1)
