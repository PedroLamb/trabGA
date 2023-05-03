class Usuario():
    def __init__(self,nomeUsuario,senha):
        self._nomeUusario= nomeUsuario
        self._senha= senha
    def cadastrar(self,nomeUsuario,senha):
        self._nomeUsuario = nomeUsuario
        self._senha= senha  #adicionar limitador
    def getnome(self):
        return self._nomeUusario
    def getsenha(self):
        return self._senha
    def login(self):
        dono= '0'
        senhaCadastrada= '0'
        while dono!=self._nomeUsuario or senhaCadastrada!= self._senha:
            dono=input('Digite seu nome de usuario: ')
            senhaCadastrada= input('Digite sua senha:')



nome= input('Informe seu nome: ')   
senha=input('Digite sua senha: ')         
a= Usuario(nome, senha)
a.cadastrar(nome,senha)
print(a.getnome()) 
print(a.getsenha())     
a.login()      

