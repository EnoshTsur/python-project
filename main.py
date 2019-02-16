import mysql.connector
from books_model.dbdao import BooksDBAO
from author_model.dbdao import AuthorDBDAO

from  author_model.author import Author
from books_model.book import Book

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="db",
        pool_name="cp",
        pool_size=10
    )

    book_db = BooksDBAO(db=mydb)
    author_db = AuthorDBDAO(db=mydb)
    # book = book_db.create_book(name="Easy Python", author="Enosh")
    # book_db.create_book(8, 'k')
    #
    # book = book_db.find_by_id('jo')
    # book = book_db.find_by_id(89)
    # book = book_db.find_by_id(4)
    # print(book)
    #
    # book_db.find_by_name("joh")
    # book = book_db.find_by_name('Easy Python')
    # print(book)
    #
    # book = Book(name='Easy JavaScript', author='Enosh', id=4)
    # book_db.update_book(7)
    # updated_book = book_db.update_book(book)
    # print(updated_book)
    #
    # all_books = book_db.find_all()
    # print(all_books)
    #
    # book_db.remove_book('k')
    # deleted_book = book_db.remove_book(4)
    # print(deleted_book)
    #
    # print(book_db.find_all())
    #
    # book_db.create_table()
    # author_db.create_table()

    # author_to_update = Author(id=90, first_name='Dana', last_name='Dvorin')
    # author = author_db.update_author(author_to_update)
    # print(author)

    # authors = author_db.find_all()
    # print(authors)

    # author = Author(id=1, first_name='Enosh', last_name='Tsur')
    # book = book_db.create_book(name='Easy JS', price=99.90, author=author)
    # print(book)
    # book = book_db.find_by_id(1)

    # book = book_db.update_book(Book(name='Easy JavaScript', price=99.90, id=1))
    # print(book)

    # book = book_db.remove_book(1)
    # print(book)

    print(author_db.find_authors_books(1))

except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")