import json

class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.status = "Pendente"
        self.prioridade = prioridade

    def marcar_completa(self):
        self.status = "Completa"

    def __str__(self):
        return f"{self.descricao} [{self.prioridade}] - {self.status}"

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "status": self.status,
            "prioridade": self.prioridade
        }

    @classmethod
    def from_dict(cls, d):
        tarefa = cls(d["descricao"], d["prioridade"])
        tarefa.status = d["status"]
        return tarefa
