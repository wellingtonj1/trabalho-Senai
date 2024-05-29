from GerenciadorDeTarefas import GerenciadorDeTarefas
from Tarefa import Tarefa

def menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Marcar tarefa como completa")
    print("4. Listar tarefas")
    print("5. Salvar dados")
    print("6. Carregar dados")
    print("7. Sair")

def main():
    gerenciador = GerenciadorDeTarefas()
    gerenciador.carregar_dados()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Baixa, Média, Alta): ")
            tarefa = Tarefa(descricao, prioridade)
            gerenciador.adicionar_tarefa(tarefa)
        elif opcao == "2":
            descricao = input("Descrição da tarefa a remover: ")
            gerenciador.remover_tarefa(descricao)
        elif opcao == "3":
            descricao = input("Descrição da tarefa a marcar como completa: ")
            for tarefa in gerenciador.tarefas:
                if tarefa.descricao == descricao:
                    tarefa.marcar_completa()
                    break
        elif opcao == "4":
            gerenciador.listar_tarefas()
        elif opcao == "5":
            gerenciador.salvar_dados()
        elif opcao == "6":
            gerenciador.carregar_dados()
        elif opcao == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
