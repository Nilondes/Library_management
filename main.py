import json


def list_books() -> list:
    """Returns a list of dictionaries with keys "id", "title", "author", "year", "status" """
    with open('data.json', 'r') as file:
        books = json.load(file)
    return books


def add_book(title, author, year) -> None:
    """Add a new item to book list. The id is determined based on last id or 0 if empty."""
    books = list_books()
    last_id = 0 if len(books) == 0 else books[len(books) - 1]["id"]
    data = {"id": last_id + 1, "title": title, "author": author, "year": year, "status": "present"}
    books.append(data)
    with open('data.json', 'w') as file:
        json.dump(books, file)


def remove_book(book_id) -> bool:
    """Remove book with specified id or return False if there is no such id in the list"""
    books = list_books()
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(i)
            with open('data.json', 'w') as file:
                json.dump(books, file)
            return True
    return False


def change_status(book_id) -> bool:
    """Change book status with specified id or return False if there is no such id in the list"""
    books = list_books()
    for i, book in enumerate(books):
        if book["id"] == book_id:
            current_book = books.pop(i)
            if current_book['status'] == 'present':
                current_book['status'] = 'given'
            else:
                current_book['status'] = 'present'
            books.insert(i, current_book)
            with open('data.json', 'w') as file:
                json.dump(books, file)
            return True
    return False


def search_book(title=None, author=None, year=None) -> list:
    """
    Returns a list of dictionaries with keys "id", "title", "author", "year", "status".
    The search is considered as match if all criteria are satisfied.
    Empty criterion is considered as "any"
    """
    books = list_books()
    result = []
    search_criteria = [['title', title], ['author', author], ['year', year]]
    for book in books:
        for criterion in search_criteria:
            if criterion[1] and book[criterion[0]] != criterion[1]:
                break
        else:
            result.append(book)
    return result


if __name__ == "__main__":
    welcome_message = """Please, enter command from the list:\n          
    - list (shows all available books)
    - add (add a book)
    - remove (remove the book)
    - change (changes book status)
    - search (search books)
    - exit (exit the library)
    """
    print(welcome_message)
    while True:
        command = input().strip().lower()
        if command == 'exit':
            print('Good bye!')
            break
        if command not in ["list", "add", "remove", "change", "search"]:
            print(f"Unknown command.\n {welcome_message}")
        else:
            if command == "list":
                all_books = list_books()
                if not all_books:
                    print('The library is empty!')
                else:
                    for a_book in all_books:
                        print(f'{a_book["id"]} - {a_book['title']} - {a_book['author']} - {a_book['year']} - {a_book['status']}')

            elif command == "add":
                try:
                    title = input('Please, enter Title: ').strip()
                    author = input('Please, enter Author: ').strip()
                    year = input('Please, enter Year: ').strip()
                    int(year)
                    add_book(title, author, year)
                    print(f'The book {title} written by {author} in {year} has been added to the library')
                except ValueError:
                    print('The year should be integer')

            elif command == "remove":
                try:
                    book_id = int(input("Please, enter the book id: ").strip())
                    if remove_book(book_id):
                        print(f"The book with id {book_id} has been removed")
                    else:
                        print(f"There is no book with id {book_id}")
                except ValueError:
                    print('The id should be integer')

            elif command == "change":
                try:
                    book_id = int(input("Please, enter the book id: ").strip())
                    if change_status(book_id):
                        print(f"The status of the book with id {book_id} has been changed")
                    else:
                        print(f"There is no book with id {book_id}")
                except ValueError:
                    print('The id should be integer')

            elif command == "search":
                title = input('Please, enter Title (or leave empty): ').strip()
                author = input('Please, enter Author (or leave empty): ').strip()
                year = input('Please, enter Year (or leave empty): ').strip()
                if year:
                    try:
                        int(year)
                    except ValueError:
                        print('The year should be integer')
                searched_books = search_book(title, author, year)
                if not searched_books:
                    print('There are no books with these criteria')
                else:
                    for a_book in searched_books:
                        print(f'{a_book["id"]} - {a_book['title']} - {a_book['author']} - {a_book['year']} - {a_book['status']}')
