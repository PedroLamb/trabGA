class Usuario():
    def __init__(self,nomeUsuario,senha):
        self._nomeUusario= nomeUsuario
        self._senha= senha
    def cadastrar(self):
        self._nomeUsuario = nome
        self._senha= senha  #adicionar limitador
    def getnome(self):
        return self._nomeUusario

nome= input('Informe seu nome: ')   
senha=input('Digite sua senha: ')         
a= Usuario(nome, senha)
a.cadastrar()
print(a.getnome())            