import os

def menu():
    os.system('cls')
    print('----------------| NBA Album |----------------')
    print('1 - Novo Álbum')
    print('2 - Acessar Album')
    print('0 - Sair da aplicação\n')
    item = input('Escolha uma opção: ')
    return item