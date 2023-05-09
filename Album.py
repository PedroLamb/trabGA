import random
import csv

albumAtual = []
usuarioAtual = []
colecaoAtual = []

def verAlbum():
    tamanhoPag = 5
    numPagina = (len(albumAtual))//tamanhoPag
    paginaAtual = 0

    while True:
        if paginaAtual == 0:
            print("Album de Figurinhas")
        else:
            indexInicio = 1 + (paginaAtual-1)*tamanhoPag
            indexFinal=indexInicio + tamanhoPag

            pagina = albumAtual[indexInicio:indexFinal]

            print(f"Página {paginaAtual}:")
            for conteudo in pagina:
                print(conteudo)

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
