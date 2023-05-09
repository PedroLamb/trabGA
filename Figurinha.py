class Figurinha:
    def __init__(self,nro,nome,conteudo,nroPagina):
        self.nro = nro
        self.nome = nome
        self.conteudo = conteudo
        self.status = None
        self.nroPagina = nroPagina

    def __str__(self):
        return f"Figurinha nro {self.nro+1}: '{self.nome}', Conteúdo: {self.conteudo}"


    def imprimir(self):
        print(self.nro,' ',self.nome,' ', self.conteudo, ' ', self.nroPagina)