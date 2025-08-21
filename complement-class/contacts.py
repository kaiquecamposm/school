import json
import os

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
      print("Erro ao carregar os contatos. O arquivo pode estar corrompido.")
      return {}
  return {}

def save_contacts(contacts):
  with open(DB_PATH, "w", encoding="utf-8") as archive:
    json.dump(contacts, archive, indent=2, ensure_ascii=False)

def add_contact(contacts):
  if os.path.exists(DB_PATH):
    name = input("Digite o nome do contato: ").strip() 

    if name in contacts:
      print(f"O contato '{name}' já existe")
      return

    tel = input("Digite o telefone: ").strip()
    mail = input("Digite o e-mail: ").strip()

    contacts[name] = {"telefone": tel, "email": mail}
    save_contacts(contacts)

def list_contacts(contacts):
  load_contacts()

      
contacts = []

while True:
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
      case _:
          print("Essa opção não existe. Aprenda a ler.")
          break
  except ValueError:
    print("Essa opção não existe. Aprenda a ler.")
