import random
import csv

albumAtual = []
usuarioAtual = []
colecaoAtual = []

def verAlbum():
    print(albumAtual)

def verColecao():
    quantidadeFigurinhas = {}
    for figurinha in colecaoAtual:
        if figurinha in quantidadeFigurinhas:
            quantidadeFigurinhas[figurinha] += 1
        else:
            quantidadeFigurinhas[figurinha] = 1
    for figurinha, quantidade in quantidadeFigurinhas.items():
        print("Figurinha {}: x{}".format(figurinha, quantidade))


def abrirPacote():
    figurinha1 = random.randint(1,15)
    figurinha2 = random.randint(1,15)
    figurinha3 = random.randint(1,15)
    colecaoAtual.append(figurinha1)
    colecaoAtual.append(figurinha2)
    colecaoAtual.append(figurinha3)
    print ('As figurinhas {},{} e {} foram adicionadas à coleção.'.format(figurinha1, figurinha2, figurinha3))
    with open(usuarioAtual[0] + ' - Colecao.csv', mode = 'a', newline = '') as colecaoArq:
        writer = csv.writer(colecaoArq)
        for i in colecaoAtual:
            writer.writerow([i])
def colarFigurinha(numeroFigurinha,colecaoAtual, albumAtual):
    numeroFigurinha= input('Qual o numero da figurinha que você quer colar? ')
    if [numeroFigurinha] == False in albumAtual and [numeroFigurinha]== True in colecaoAtual:
        colecaoAtual=numeroFigurinha-1 
        numeroFigurinha in albumAtual is True
    else:
        print("Figurinha não encontrada na coleção ou já está colada no álbum.")
    #   if numeroFigurinha in colecaoAtual and not colecaoAtual[numeroFigurinha]:
    #      colecaoAtual[numeroFigurinha] = True
    #      albumAtual[numeroFigurinha] = True
    #      print("Figurinha colada com sucesso!")
    #      abrir_menu_anterior()
    #   else:
         
    #      abrir_menu_anterior()
