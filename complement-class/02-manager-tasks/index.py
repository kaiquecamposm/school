import sys


def show_menu():
  print("\nMenu:")
  print("1. Adicionar tarefa")
  print("2. Marcar tarefa como concluída")
  print("3. Listar tarefas pendentes")
  print("4. Listar tarefas concluídas")
  print("5. Sair")

def add_task(list): 
  task = input("Digite o nome da tarefa para adicionar na lista: ").strip()

  if any(task == item['description'] for item in list):
    print(f"A tarefa '{task}' já está na lista.")
  else:
    list.append({"description": task, "completed": False})
    print(f"Tarefa '{task}' adicionada com sucesso!")

def mark_completed_task(list):
  task = input("Digite o nome da tarefa concluída: ").strip()

  for item in list:
    if task == item["description"]:
      if item["completed"]:
        print(f"A tarefa '{task}' já foi concluída")
      else:
        item["completed"] = True
        print(f"A tarefa '{task}' foi concluída")

def list_tasks(list, completed):
  status = "concluídas" if completed else "pendentes"
  tasks = [item["description"] for item in list if item["completed"] == completed]

  if tasks:
    print(f"\nTarefas {status}:")
    for i, item in enumerate(list, start = 1):
      print(f"{i}. {item["description"]}") 
  else:
    print(f"Não há tarefas {status} no momento.")

tasks = []

while True:
  show_menu()

  try: 
    option = int(input("\nEscolha uma opção:").strip())
    
    match option:
      case 1:
        add_task(tasks)
      case 2:
        mark_completed_task(tasks)
      case 3:
        list_tasks(tasks, completed = False)
      case 4:
        list_tasks(tasks, completed = True)
      case 5:
        print("Encerrando o programa. Tchau!")
        sys.exit()
      case _:
        print("Essa opção não existe. Aprenda a ler.")
        break
  except ValueError:
    print("Essa opção não existe. Aprenda a ler.")
