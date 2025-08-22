import json
import os
import sys

DB_PATH = 'contacts.json'

def show_menu():
  print("\nMenu:")
  print("1. Adicionar contato")
  print("2. Remover contato")
  print("3. Listar contatos")
  print("4. Sair")

def load_contacts():
  if os.path.exists(DB_PATH):
    try:
      with open(DB_PATH, "r", encoding="utf=8") as archive:
        return json.load(archive)
    except json.JSONDecodeError:
      print("Erro ao carregar os dados. O arquivo pode estar corrompido.")
      return {}
  return {}

def save_contacts(contacts):
  with open(DB_PATH, "w", encoding="utf-8") as archive:
    json.dump(contacts, archive, indent=2, ensure_ascii=False)

def add_contact(contacts):
  name = input("Digite o nome do contato: ").strip() 

  if name in contacts:
    print(f"O contato '{name}' já existe")
    return

  tel = input("Digite o telefone: ").strip()
  mail = input("Digite o e-mail: ").strip()

  contacts[name] = {"telefone": tel, "email": mail}
  save_contacts(contacts)
  print(f"Contato '{name}' adicionado com sucesso.")
    

def remove_contact(contacts):
  name = input("Digite o nome do contato: ").strip()

  if name in contacts:
    del contacts[name]
    save_contacts(contacts)
    print(f"Contato '{name}' removido com sucesso.")
  else:
    print(f"O contato '{name}' não foi encontrado.")

def list_contacts(contacts):
  if contacts:
    print("\nLista de Contatos:")
    for name, data, in contacts.items():
      print(f"Nome: {name}, Telefone: {data['telefone']}, Email: {data['email']}")
  else:
    print("Nenhum contato encontrado.")

contacts = load_contacts()

while True:
  show_menu()

  try:
    option = int(input("Escolha uma opção:").strip())

    match option:
      case 1:
        add_contact(contacts)
      case 2:
        remove_contact(contacts)
      case 3:
        list_contacts(contacts)
      case 4:
        print("Encerrando o programa. Tchau!")
        sys.exit()
      case _:
          print("Essa opção não existe. Aprenda a ler.")
          break
  except ValueError:
    print("Essa opção não existe. Aprenda a ler.")
