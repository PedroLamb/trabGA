import os

def menuInicial():
    os.system('cls')
    print('----------------| NBA Album - Início |----------------')
    print('1 - Novo Álbum')
    print('2 - Acessar Album')
    print('0 - Sair da aplicação\n')
    item = input('Escolha uma opção: ')
    return item

def menuGerenciamentoAlbum():
    os.system('cls')
    print('----------------| NBA Album |----------------')
    print('1 - Ver Álbum')
    print('2 - Gerenciar coleção')
    print('3 - Abrir pacote')
    print('0 - Retornar à tela inicial\n')
    item = input('Escolha uma opção')
    return item

def menuGerenciamentoColecao():
    os.system('cls')
    print('----------------| NBA Album - Coleção |----------------')   
    print('1 - Colar figurinha')
    print('2 - Disponibilizar para troca')
    print('3 - Propor troca')
    print('4 - Revisar solicitações')
    print('0 - Voltar para a tela de gerenciamento do álbum\n')
    item = input('Escolha uma opção: ')
    return item