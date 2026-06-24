def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade (1-5 , 1= mais alta): ")

    while not (prioridade.isdigit() and 1 <= int(prioridade) <= 5):
        print("por favor , digite um numero de 1 a 5 :")
        prioridade = (input("Prioridade (1-5 , 1= mais alta): "))

        tarefa = {
          "descrição":descricao,
          "prioridade":int(prioridade),
          "status":"pendente"
     }
    
        tarefas.append(tarefas)

def pegar_prioridade (tarefa):
     return tarefa["prioridade"]

def listar_tarefas(tarefa):

    if len(tarefa) == 0:
         print("nenhuma tarefa cadastrada.")
         return
    
    tarefa.sort(key=pegar_prioridade)

    print("\nTarefa:")
    for i in range(len(tarefa)):
        t = tarefa[i]
        print(f"-{i +1}. {t["descrição"]} (Prioridade: {i["prioridade"]}) - status: Pendente\n")




def Marcar_concluida(tarefas):
     if len(tarefas) == 0:
         print("nenhuma tarefa para marcar.")
         return
     

def main():
    tarefas = []
    while True:
        print("\nMENU:")
        print("1- Adicionar Tarefa")
        print("2- Listar Tarefas")
        print("3- Marcar Tarefa como concluida")
        print("4- Excluir Tarefa")
        print("5- Sair")

        escolha = input("Escolha uma opção:")

        if escolha == "1":
             adicionar_tarefa(tarefas)
        elif escolha == "2":
             listar_tarefas(tarefas)
        elif escolha == "3":
             Marcar_concluida(tarefas)
        elif escolha == "4":
          excluir_tarefa(tarefas)
        elif escolha == "5":
             print("Saindo do Programa , até mais ...")
             break
        else:
             print("Opção Inválida ! Tente Novamente.")

if __name__ == "__main__":
        main()