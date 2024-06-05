import usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuario = []
    
    def adicionar_livros(self,Livros):
        self.livros.append(Livros)

    def remover_livros(self, titulo):
        self.livros.remove()

    def listar_livros(self):
        for livro in self.livros:
             print(livro.__dict__)
    def emprestar_livro(self, titulo, usuario):
       for livro in self.livros:
           if livro.titulo == titulo:
               if livro.disponivel == True:
                   livro.disponivel = False
                   for user in self.usuario:
                       if user.nome == usuario:
                           user.livro_emprestado.append(livro)
    #def devolver_livro(self, titulo):
        #for livro in livro_emprestado:
            #if livro.titulo == True

    
    def salva_dados(self,nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.usuario.append()

    def carrega_dados(self, nome, email, idade):
        print(self.usuario)

    def lista_de_livros_emprestados(self):
        for livro in self.livros:
            if livro.disponivel == True:
                print(livro.titulo,'Livros Disponivel')
            if livro.disponivel == False:
                print(livro.titulo,'Livro indisponivel')
                