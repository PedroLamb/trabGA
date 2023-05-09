import random
import csv
import os
import math

albumAtual = []
usuarioAtual = []
colecaoAtual = []

def verAlbum(aplicacao):
    os.system('cls')
    with open('./Albuns/' + usuarioAtual[0] + ' - Album.csv', mode='r') as albumArq:
        reader = csv.reader(albumArq)
        albumAtual = [item[0] for item in list(reader)]
    tamanhoPag = 5
    numPagina = (len(albumAtual))//tamanhoPag
    paginaAtual = 0

    while True:
        os.system('cls')
        if paginaAtual == 0:
            print("Album de Figurinhas")
        else:
            os.system('cls')
            indexInicio = (paginaAtual-1)*tamanhoPag
            indexFinal = indexInicio + tamanhoPag

            pagina = albumAtual[indexInicio:indexFinal]

            print(f"Página {paginaAtual}:")
            for indice, conteudo in enumerate(pagina):
                if conteudo == 'True':
                    print(aplicacao.listaFigurinhas[(indexInicio + indice)])
                else:
                    print('X')

        trocaPagina = input("Quer avançar pra próxima página? (voltar/próximo) ")

        if trocaPagina.lower() == "próximo":
            if paginaAtual < numPagina:
                paginaAtual+=1
            else:
                print("Você está na última página.")
        elif trocaPagina.lower() == "voltar":
            if paginaAtual > 0:
                paginaAtual-=1
            else:
                print("Você está na primeira página.")
        elif trocaPagina.lower() == "sair":
            break
        else:
            print("Inválido, tente novamente.")

        


def verColecao():
    os.system('cls')
    print('----------------GERENCIAR COLECAO----------------')
    quantidadeFigurinhas = {}
    for i in colecaoAtual:
        if i in quantidadeFigurinhas:
            quantidadeFigurinhas[i] += 1
        else:
            quantidadeFigurinhas[i] = 1
    for i, quantidade in quantidadeFigurinhas.items():
        print("Figurinha {}: x{}".format(i, quantidade))
    print(colecaoAtual)
    print('1 - Colar figurinha')
    print('2 - Disponibilizar para troca')
    print('3 - Propor troca')
    print('4 - Revisar solicitacoes')
    print('0 - Voltar para a tela Gerenciar Album\n')
    item = input('Escolha uma opcao: ')
    return item


def abrirPacote():
    
    figurinha1 = random.randint(1,15)
    figurinha2 = random.randint(1,15)
    figurinha3 = random.randint(1,15)
    colecaoAtual.append(figurinha1)
    colecaoAtual.append(figurinha2)
    colecaoAtual.append(figurinha3)
    print ('As figurinhas {},{} e {} foram adicionadas à coleção.'.format(figurinha1, figurinha2, figurinha3))
    with open('./Colecoes/' + usuarioAtual[0] + ' - Colecao.csv', mode = 'a', newline = '') as colecaoArq:
        writer = csv.writer(colecaoArq)
        for i in colecaoAtual:
            writer.writerow([i])


def colarFigurinha():
    with open('./Albuns/' + usuarioAtual[0] + ' - Album.csv', mode='r') as albumArq:
        reader = csv.reader(albumArq)
        albumAtual = [item[0] for item in list(reader)]

    with open('./Colecoes/' + usuarioAtual[0] + ' - Colecao.csv', mode='r') as colecaoArq:
        reader = csv.reader(colecaoArq)
        colecaoAtual = [int(item[0]) for item in list(reader)]
        numeroFigurinha = int(input('Qual o número da figurinha que você quer colar? '))
    if numeroFigurinha in colecaoAtual:
        if albumAtual[numeroFigurinha - 1] == 'False':
            albumAtual[numeroFigurinha - 1] = 'True'
            colecaoAtual.remove(numeroFigurinha)
            print(f"Figurinha {numeroFigurinha} colada com sucesso!")
            with open('./Albuns/' + usuarioAtual[0] + ' - Album.csv', mode='w', newline='') as albumArq:
                writer = csv.writer(albumArq)
                for i in range(len(albumAtual)):
                    writer.writerow([albumAtual[i]])
            with open('./Colecoes/' + usuarioAtual[0] + ' - Colecao.csv', mode='w', newline='') as colecaoArq:
                writer = csv.writer(colecaoArq)
                for i in range(len(colecaoAtual)):
                    writer.writerow([colecaoAtual[i]])
            albumArq.close()
            colecaoArq.close()
            print("Posição a ser colada no álbum:", numeroFigurinha - 1)
    else:
        print("Figurinha não encontrada na coleção ou já está colada no álbum.")
    input('Pressione ENTER para prosseguir...')
    #   if numeroFigurinha in colecaoAtual and not colecaoAtual[numeroFigurinha]:
    #      colecaoAtual[numeroFigurinha] = True
    #      albumAtual[numeroFigurinha] = True
    #      print("Figurinha colada com sucesso!")
    #      abrir_menu_anterior()
    #   else:
         
    #      abrir_menu_anterior()
