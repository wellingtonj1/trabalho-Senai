from biblioteca import Biblioteca
from livros import Livro
from usuario import Usuario
import re

def validar_nome(nome):
    # Expressão regular para garantir que o nome contenha apenas letras e espaços
    padrao = r'^[a-zA-Z\s]+$'
    if re.match(padrao, nome):
        return True
    else:
        return False



if __name__ == "__main__":
    biblio = Biblioteca()
    print('Ola, bem vindo a biblioteca')

    
    cada1 = Usuario()
    biblio.usuario.append(cada1)
    #print(biblio.usuario)
    #biblio.livros.append()
    #print(biblio.livros)
    
    while True:
        add = input('deseja adicionar um livro? (sim/nao) ').upper()
        if add == 'SIM':
            tiltle = input('titulo: ''Digite o titulo do livro que deseja adicionar: ')
            ano_do_livro = input('Ano do livro: '' digite o ano que o livro foi publicado: ')
            autor = input('Autor: ' 'digite o nome do autor do livro: ')
            livro1 = Livro(tiltle,autor, ano_do_livro)
            biblio.adicionar_livros(livro1)

        elif add == 'NAO':
            break
    
    emprestar = input('deseja pega um livro emprestado (sim/nao) ').upper()
    if emprestar == 'SIM':
        print('Lista de livros disponiveis: \n' ) 
        biblio.listar_livros()
        titulo = input('digite o nome do livro que deseja pegar emprestado: ')
        usuario = input('digite o nome do usuario que deseja pegar o livro: ')
        biblio.emprestar_livro(titulo, usuario)
    elif emprestar == 'NAO':
        pass

    ver_livros = input('Deseja ver lista de livros Disponiveis ou Indisponiveis (sim/nao) ').upper()
    if ver_livros == 'SIM':
        biblio.lista_de_livros_emprestados()
    elif ver_livros == 'NAO':
        pass

    