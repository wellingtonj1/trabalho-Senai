from biblioteca import Biblioteca
from livros import Livro
from usuario import Usuario

if __name__ == "__main__":
    biblio = Biblioteca()
    print('Ola, bem vindo a biblioteca')

    usuario1 = input('digite seu nome para cadastro Somente letras: ')
    while True:
        if usuario1.isalpha():
            break   
        else:
            usuario1 = input('Nome invalido pois contem numeros, digite novamente: ')
        
    email1 = input('digite seu email: ')
    idade1 = int(input('digite sua idade: '))
    cada1 = (usuario1, email1, idade1)
    biblio.usuario.append(cada1)
    #print(biblio.usuario)
    #biblio.livros.append()
    print(biblio.livros)
    
    while True:
        add = input('deseja adicionar um livro? (sim/nao) ')
        if add == 'sim':
            tiltle = input('titulo: ''Digite o titulo do livro que deseja adicionar: ')
            ano_do_livro = input('Ano do livro: '' digite o ano que o livro foi publicado: ')
            autor = input('Autor: ' 'digite o nome do autor do livro: ')
            #livro1 = (tiltle, ano_do_livro, autor)
            biblio.livros.append(tiltle)
            biblio.livros.append(ano_do_livro)
            biblio.livros.append(autor)
            print(biblio.livros)

        elif add == 'nao':
            break
    
    emprestar = input('deseja pega um livro emprestado (sim/nao) ')
    if emprestar == 'sim':
        print('Lista de livros disponiveis: ''\n' ,biblio.livros)  
        titulo = input('digite o nome do livro que deseja pegar emprestado: ')
        usuario = input('digite o nome do usuario que deseja pegar o livro: ')
    elif emprestar == 'nao':
        pass
    if titulo in biblio.livros:
        #biblio.livros(biblio.remover_livros)
        print('livro emprestado com sucesso')
    else:
         print('livro indisponivel')

    #devolver = input('deseja devolver um livro (sim/nao) ')
    print(biblio.livros)

    
    