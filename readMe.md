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
