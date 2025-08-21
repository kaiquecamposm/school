def show_menu():
  print("\nMenu:")
  print("1. Adicionar item")
  print("2. Remover item")
  print("3. Listar itens")
  print("4. Sair")

def add_item(list):
  item = input("Digite o nome do item para adicionar na lista: ").strip()

  if item in list:
      print(f"O item '{item}' já está na lista.")
  else:
      list.append(item)
      print(f"Item '{item}' adicionado com sucesso!")

def remove_item(list):
  item = input("Digite o nome do item para excluir da lista: ").strip()

  if item in list:
    print(f"O item '{item}' já está na lista.")
  else:
    list.append(item)
    print(f"Item '{item}' adicionado com sucesso!")

def list_items(list):
  if list:
    print("\nItens na lista de compras:")
    for i, item in enumerate(list, start = 1):
      print(f"{i}. {item}") 
  else:
    print("A lista está vazia.")

shop_list = []

while True:
  show_menu()

  try:
    option = int(input("Escolha uma opção: "))

    if option == 1:
      add_item(list)
    elif option == 2:
      remove_item(list)
    elif option == 3:
      list_items(list)
    elif option == 4:
      print("Encerrando o programa. Tchau!")
      break
    else:
      print("Essa opção não existe. Aprenda a ler.")
  except ValueError:
      print("Essa opção não existe. Aprenda a ler.")