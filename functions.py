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