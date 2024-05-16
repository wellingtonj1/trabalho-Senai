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
   - Crie pelo menos duas contas bancárias.
   - Realize operações de depósito, saque e transferência.
   - Exiba os saldos das contas.
   - Salve e carregue os dados das contas.

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



