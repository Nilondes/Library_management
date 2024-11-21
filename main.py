import json, unittest


test_case = [{"id": 1, "title": "test title", "author": "Test Author", "year": "1986", "status": "present"}]


def list_books() -> list:
    with open('data.json', 'r') as file:
        books = json.load(file)
    return books


def add_book(title, author, year):
    books = list_books()
    last_id = books[len(books) - 1]["id"]
    data = {"id": last_id + 1, "title": title, "author": author, "year": year, "status": "present"}
    books.append(data)
    with open('data.json', 'w') as file:
        json.dump(books, file)


def remove_book(book_id):
    books = list_books()
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(i)
            with open('data.json', 'w') as file:
                json.dump(books, file)
            return True
    return False


def change_status(book_id):
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


def search_book(title=None, author=None, year=None):
    books = list_books()
    result = []
    if title:
        search_criteria = ['title', title]
    elif author:
        search_criteria = ['author', author]
    elif year:
        search_criteria = ['year', year]
    for book in books:
        if book[search_criteria[0]] == search_criteria[1]:
            result.append(book)
    return result

