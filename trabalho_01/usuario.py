import re

class Usuario:
    def __init__(self):
        self.nome = input('digite seu nome para cadastro Somente letras: ')
        while not self.validar_nomes():
            self.nome = input('Nome invalido pois contem numeros, digite novamente: ')
        self.livro_emprestado = []

    def validar_nomes(self):
        # Expressão regular para garantir que o nome contenha apenas letras e espaços
        padrao = r'^[a-zA-Z\s]+$'
        if re.match(padrao, self.nome):
            return True
        else:
            return False

