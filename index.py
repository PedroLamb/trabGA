class Usuario():
    def __init__(self, nomeUsuario, senha, album):
        self._nomeUsuario= nomeUsuario
        self._senha= senha
        self._album='?'
    def getnome(self):
        return self._nomeUsuario
    
print('alo mundo')