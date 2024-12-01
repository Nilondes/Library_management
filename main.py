from functions import list_books, add_book, remove_book, change_status, search_book


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
