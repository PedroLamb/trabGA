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
