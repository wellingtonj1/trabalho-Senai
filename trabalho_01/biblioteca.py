class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuario = []
    
    def adicionar_livros(self,Livros):
        self.livros.append()

    def remover_livros(self, titulo):
        self.livros.remove()

    def listar_livros(self, ver_livros):
        for lista in self.livros:
             print(lista.__dict__)
    def emprestar_livro(self, titulo, nome):
        livro_encontrado = None
        for livro in self.livros:
            if titulo == livro.titulo:
                livro_encontrado = livro
        # verificar se livro_encontrado exise e não None.. e verificar se ta disponivel