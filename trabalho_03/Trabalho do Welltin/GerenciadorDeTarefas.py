import json
from Tarefa import Tarefa

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, descricao):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.descricao != descricao]

    def listar_tarefas(self):
        tarefas_ordenadas = sorted(self.tarefas, key=lambda t: t.prioridade, reverse=True)
        for tarefa in tarefas_ordenadas:
            print(tarefa)

    def salvar_dados(self):
        with open('tarefas.json', 'w') as f:
            json.dump([tarefa.to_dict() for tarefa in self.tarefas], f)

    def carregar_dados(self):
        try:
            with open('tarefas.json', 'r') as f:
                tarefas_dict = json.load(f)
                self.tarefas = [Tarefa.from_dict(d) for d in tarefas_dict]
        except FileNotFoundError:
            self.tarefas = []
