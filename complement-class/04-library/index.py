import json
import os
import sys

DB_PATH = "books.json"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Livro '{title}' adicionado à biblioteca.")

    def list_available_books(self):
        available = [book for book in self.books if not book.borrowed]

        if available:
            print("\nLivros Disponíveis: ")
            for book in available:
                print(f"- {book}")
        else:
            print("Nenhum livro disponível no momento.")

    def list_borrowed_books(self):
        borrowed = [book for book in self.books if book.borrowed]

        if borrowed:
            print("\nLivros Emprestados: ")
            for book in borrowed:
                print(f"- {book}")
        else:
            print("Nenhum livro emprestado no momento.")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrowed = True
                print(f"O livro '{book}' foi emprestado com sucesso.")
            else:
                print(f"O livro '{title}' já foi emprestado.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrowed = False
                print(f"O livro '{book}' foi devolvido com sucesso.")
            else:
                print(f"O livro '{title}' já foi devolvido.")


def show_menu():
    print("\nMenu: ")
    print("1. Adicionar Livro")
    print("2. Listar Livros disponíveis")
    print("3. Listar Livros Emprestados")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Sair")


library = Library()

while True:
    show_menu()
    option = int(input("Escolha uma opção: ").strip())

    match option:
        case 1:
            title = input("Digite o nome do livro: ").strip()
            author = input("Digite o nome do autor do livro: ").strip()

            library.add_book(title, author)
        case 2:
            library.list_available_books()
        case 3:
            library.list_borrowed_books()
        case 4:
            title = input("Digite o nome do livro: ").strip()

            library.lend_book(title)
        case 5:
            title = input("Digite o nome do livro: ").strip()

            library.return_book(title)
        case 6:
            print("Encerrando o programa. Tchau.")
            sys.exit()
