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


### Trabalho 2: Sistema de Gerenciamento de Contas Bancárias com Transferências e Persistência de Dados

**Descrição:**
Implemente um sistema de gerenciamento de contas bancárias que permita criar contas, depositar, sacar, verificar saldo e realizar transferências entre contas. Os dados das contas devem ser salvos em arquivos para que possam ser carregados posteriormente.

**Requisitos:**
1. Crie a classe `ContaBancaria` no arquivo `ContaBancaria.py` com os seguintes atributos:
   - `numero`
   - `titular`
   - `saldo` (inicialmente 0)

2. Adicione os seguintes métodos à classe `ContaBancaria`:
   - `depositar(valor)`
   - `sacar(valor)`
   - `exibir_saldo()`
   - `transferir(valor, conta_destino)`
   - `to_dict()`: Retorna um dicionário representando a conta.
   - `from_dict(d)`: Cria uma conta a partir de um dicionário.

3. Crie uma classe `Banco` no arquivo `Banco.py` com os seguintes métodos:
   - `adicionar_conta(conta)`
   - `remover_conta(numero)`
   - `buscar_conta(numero)`
   - `salvar_dados()`
   - `carregar_dados()`

4. Crie um script `main.py` que:
   - Permita Criar contas bancárias.
   - Permita Realizar operações de depósito, saque e transferência.
   - Permita Exibir os saldos das contas.
   - Permita Salvar e carregar os dados das contas.

**Estrutura de Arquivos:**
```
trabalho_02/
    ContaBancaria.py
    Banco.py
    main.py
```

**Código de Exemplo:**

**ContaBancaria.py**
```python

class ContaBancaria:
    def __init__(self, numero, titular):
        pass
    
```

**Banco.py**
```python
from ContaBancaria import ContaBancaria

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        pass

    def remover_conta(self, numero):
        pass

    def buscar_conta(self, numero):
        pass

    def salvar_dados(self):
        pass

    def carregar_dados(self):
        pass
```

**main.py**
```python
from Banco import Banco
from ContaBancaria import ContaBancaria

if __name__ == "__main__":
    banco = Banco()
    banco.carregar_dados()

    conta1 = ContaBancaria("001", "Alice")
    conta2 = ContaBancaria("002", "Bob")

    banco.adicionar_conta(conta1)
    banco.adicionar_conta(conta2)

    conta1.depositar(1000)
    conta1.sacar(250)
    conta1.exibir_saldo()

    conta2.depositar(500)
    conta1.transferir(100, conta2)
    conta2.exibir_saldo()

    conta1.exibir_saldo()
    conta2.exibir_saldo()

    banco.salvar_dados()
```

Onde os do numero da conta será um numero de 4 digitos aleatório.
E os dados do nome e dos valores a depositar e sacar deverão vir do input do usuário.




### Trabalho 3: Sistema de Gerenciamento de Tarefas com Prioridade e Persistência de Dados

**Descrição:**
Implemente um sistema de gerenciamento de tarefas onde se pode adicionar, remover, listar tarefas e definir a prioridade das tarefas. Os dados das tarefas devem ser salvos em arquivos para que possam ser carregados posteriormente.

**Requisitos:**
1. Crie a classe `Tarefa` no arquivo `Tarefa.py` com os seguintes atributos:
   - `descricao`
   - `status` (inicialmente "Pendente")
   - `prioridade` (pode ser "Baixa", "Média" ou "Alta")

2. Adicione os seguintes métodos à classe `Tarefa`:
   - `marcar_completa()`
   - `__str__()`
   - `to_dict()`: Retorna um dicionário representando a tarefa.
   - `from_dict(d)`: Cria uma tarefa a partir de um dicionário.

3. Crie uma classe `GerenciadorDeTarefas` no arquivo `GerenciadorDeTarefas.py` com os seguintes métodos:
   - `adicionar_tarefa(tarefa)`
   - `remover_tarefa(descricao)`
   - `listar_tarefas()`: Lista todas as tarefas, ordenadas por prioridade.
   - `salvar_dados()`
   - `carregar_dados()`

4. Crie um script `main.py` que:
   - Permita adicionar tarefas com diferentes prioridades.
   - Permita Remover uma tarefa.
   - Permita Marcar uma tarefa como completa.
   - Permita Listar todas as tarefas, ordenadas por prioridade.
   - Permita Salvar e carregue os dados das tarefas.

**Estrutura de Arquivos:**
```
trabalho_03/
    Tarefa.py
    GerenciadorDeTarefas.py
    main.py
```

**Código de Exemplo:**

**Tarefa.py**
```python
class Tarefa:
    def __init__(self, descricao, prioridade):
        pass

    def marcar_completa(self):
        pass

    def to_dict(self):
        pass
```

**GerenciadorDeTarefas.py**
```python
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        pass

    def remover_tarefa(self, descricao):
        pass
```

**main.py**
```python
from GerenciadorDeTarefas import GerenciadorDeTarefas
from Tarefa import Tarefa

if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    gerenciador.carregar_dados()

    tarefa1 = Tarefa("Estudar Python", "Alta")
    tarefa2 = Tarefa("Fazer exercícios", "Média")
    tarefa3 = Tarefa("Ler um livro", "Baixa")

    gerenciador.adicionar_tarefa(tarefa1)
    gerenciador.adicionar_tarefa(tarefa2)
    gerenciador.adicionar_tarefa(tarefa3)

    gerenciador.remover_tarefa("Fazer exercícios")

    tarefa1.marcar_completa()

    gerenciador.listar_tarefas()

    gerenciador.salvar_dados()
```
Onde os dados da tarefa e a prioridade da mesma deverá vir do input do usuário.
