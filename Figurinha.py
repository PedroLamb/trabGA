class Figurinha:
    def __init__(self,nro,nome,conteudo,nroPagina):
        self.nro = nro
        self.nome = nome
        self.conteudo = conteudo
        self.status = None
        self.nroPagina = nroPagina

    def imprimir(self):
        print(self.nro,' ',self.nome,' ', self.conteudo, ' ', self.nroPagina)