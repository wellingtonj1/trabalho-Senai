import usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuario = []
    
    def adicionar_livros(self,Livros):
        self.livros.append(Livros)

    def remover_livros(self, titulo):
        self.livros.remove()

    def listar_livros(self, ver_livros):
        for lista in self.livros:
             print(lista.__dict__)
    def emprestar_livro(self, titulo, usuario):
       for livro in self.livros:
           if livro.titulo == titulo:
               if livro.disponivel == True:
                   livro.disponivel = False
                   for user in self.usuario:
                       if user.nome == usuario:
                           user.livro_emprestado = livro
    def devolver_livro(self, titulo):
        self.livros.append()
    
    def salva_dados(self,nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.usuario.append()

    def carrega_dados(self, nome, email, idade):
        print(self.usuario)
    
