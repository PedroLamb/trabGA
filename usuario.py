import csv
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.album = None

    def getNomeUsuario(self):
        return self.nome()
    
    def cadastrarUsuario(self):
        self.album = [False] * 15
        with open('Usuarios.csv', mode = 'a', newline = '') as usuariosArq:
            writer = csv.writer(usuariosArq)
            writer.writerow([self.nome, self.senha])
        with open('./Albuns/' + self.nome + ' - Album.csv', mode = 'a', newline = '') as albumArq: 
            writer = csv.writer(albumArq)
            for i in range(15):
                writer.writerow([self.album[i]])
        with open('./Colecoes/' + self.nome + ' - Colecao.csv', mode = 'a', newline = '') as colecaoArq:
            writer = csv.writer(colecaoArq)
            pass


    def logarUsuario(self):
        with open('Usuarios.csv', mode = 'r', newline = '') as usuariosArq:
            reader = csv.reader(usuariosArq)
            for row in reader:
                if row [0] == self.nome and row[1] == self.senha:
                    return True
            return False
    
    def getAlbum(self):
        return self.album 
    