import unittest
from functions import list_books, add_book, remove_book, change_status, search_book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.test_book_1 = {"id": 1,
                            "title": "test title 1",
                            "author": "First Author",
                            "year": "1986",
                            "status": "present"
                            }
        self.test_book_2 = {"id": 2,
                            "title": "test title 2",
                            "author": "Second Author",
                            "year": "1986",
                            "status": "present"
                            }
        add_book(self.test_book_1["title"], self.test_book_1["author"], self.test_book_1["year"])
        add_book(self.test_book_2["title"], self.test_book_2["author"], self.test_book_2["year"])

    def tearDown(self):
        books = list_books()
        for book in books:
            remove_book(book["id"])

    def test_list_books(self):
        books = list_books()
        self.assertEqual(books[0], self.test_book_1)
        self.assertEqual(books[1], self.test_book_2)

    def test_add_book(self):
        title, author, year = "test title 3", "Third Author", "1972"
        add_book(title, author, year)
        books = list_books()
        self.assertEqual(books[2]["id"], 3)

    def test_remove_book(self):
        remove_existing_book = remove_book(1)
        remove_nonexistent_book = remove_book(1)
        books = list_books()
        self.assertTrue(remove_existing_book)
        self.assertFalse(remove_nonexistent_book)
        self.assertEqual(len(books), 1)

    def test_change_status(self):
        initial_books = list_books()
        change_existing_book = change_status(1)
        change_nonexistent_book = change_status(7)
        changed_books = list_books()
        self.assertTrue(change_existing_book)
        self.assertFalse(change_nonexistent_book)
        self.assertNotEqual(initial_books[0]["status"], changed_books[0]["status"])

    def test_search_book(self):
        books = list_books()
        empty_search_book = search_book('','','')
        title_search_book = search_book('test title 2', '', '')
        author_search_book = search_book('', 'First Author', '')
        year_search_book = search_book('', '', '1986')
        title_and_author_search_book = search_book('test title 2', 'First Author', '')
        self.assertEqual(empty_search_book, books)
        self.assertEqual(title_search_book[0], books[1])
        self.assertEqual(author_search_book[0], books[0])
        self.assertEqual(year_search_book, books)
        self.assertEqual(title_and_author_search_book, [])


if __name__ == '__main__':
    unittest.main()
