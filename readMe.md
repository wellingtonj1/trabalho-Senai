### Trabalho 1: Sistema de Biblioteca com Empréstimos e Persistência de Dados

**Descrição:**
Implemente um sistema de gerenciamento de biblioteca com funcionalidades para adicionar, remover, listar livros e gerenciar empréstimos. Os dados da biblioteca e dos usuários devem ser salvos em arquivos para que possam ser carregados posteriormente.

**Requisitos:**
1. Crie a classe `Livro` no arquivo `Livro.py` com os seguintes atributos:
   - `titulo`
   - `autor`
   - `ano`
   - `disponivel` (inicialmente `True`)

2. Crie a classe `Usuario` no arquivo `Usuario.py` com os seguintes atributos:
   - `nome`
   - `livros_emprestados` (uma lista para armazenar os livros emprestados)

3. Crie a classe `Biblioteca` no arquivo `Biblioteca.py` com os seguintes métodos:
   - `adicionar_livro(livro)`
   - `remover_livro(titulo)`
   - `listar_livros()`
   - `emprestar_livro(titulo, usuario)`
   - `devolver_livro(titulo, usuario)`
   - `salvar_dados()`: Salva os dados da biblioteca e dos usuários em arquivos.
   - `carregar_dados()`: Carrega os dados da biblioteca e dos usuários a partir de arquivos.

4. Crie um script `main.py` que:
   - Permita Adicionar livros à biblioteca.
   - Permita Criar usuários.
   - Permita Realizar operações de empréstimo e devolução.
   - Permita Listar todos os livros, indicando quais estão disponíveis e quais estão emprestados.
   - Permita Salvar e carregar os dados da biblioteca e dos usuários.

**Estrutura de Arquivos:**
```
trabalho_01/
    Livro.py
    Usuario.py
    Biblioteca.py
    main.py
```

**Código de Exemplo:**

**Livro.py**
```python
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

```

**Usuario.py**
```python
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

```

**Biblioteca.py**
```python
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        pass

    def remover_livro(self, titulo):
        pass

    def listar_livros(self):
        pass

    def emprestar_livro(self, titulo, usuario):
        pass

    def devolver_livro(self, titulo, usuario):
        pass

    def salvar_dados(self):
        pass

    def carregar_dados(self):
        pass
```

**main.py**
```python
from Biblioteca import Biblioteca
from Livro import Livro
from Usuario import Usuario

if __name__ == "__main__":
    biblio = Biblioteca()
    biblio.carregar_dados()

    livro1 = Livro("1984", "George Orwell", 1949)
    livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro3 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)

    biblio.adicionar_livro(livro1)
    biblio.adicionar_livro(livro2)
    biblio.adicionar_livro(livro3)

    usuario1 = Usuario("Alice")
    usuario2 = Usuario("Bob")

    biblio.usuarios.append(usuario1)
    biblio.usuarios.append(usuario2)

    biblio.emprestar_livro("1984", usuario1)
    biblio.emprestar_livro("O Senhor dos Anéis", usuario2)
    biblio.devolver_livro("1984", usuario1)

    biblio.listar_livros()

    biblio.salvar_dados()
```

Será necessário que os dados tanto do nome dos usuários quanto do livro venham do usuário que está executando o código no terminal

