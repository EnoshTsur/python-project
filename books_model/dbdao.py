import mysql.connector
from books_model.book import Book
from author_model.author import Author
from author_model.dbdao import AuthorDBDAO
from utils.utils import TypeUtils
from utils.utils import ErrorMsgUtils


class BooksDBAO:

    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def create_table(self):
        """
        Create Books Table
        :return:
        """
        try:
            self.cursor.execute("CREATE TABLE BOOKS "
                                "(ID INT AUTO_INCREMENT, "
                                "NAME VARCHAR(255), "
                                "PRICE DOUBLE, "
                                "AUTHOR_ID INT, "
                                "PRIMARY KEY (ID), "
                                "FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR(ID)"
                                ")")
            # Success
            print("Table Books was created successfully")

            # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def create_book(self, name, price, author):
        """
        Validates name & price & author type
        Validates Book is not exists by name
        Creates a new book into the BOOKS's table
        :param name: str
        :param price: int | float
        :param author: Author
        :return: Book | None
        """

        # Validates name
        if not TypeUtils.is_type(name, var_type=str):
            print(ErrorMsgUtils.type_error(name, var_type=str))
            return

        # Validates price
        if not TypeUtils.is_type_or(price, var_type1=int, var_type2=float):
            print(ErrorMsgUtils.none_of_type(int, float, var=print()))
            return

        # Validates author
        if not TypeUtils.is_type(author, var_type=Author):
            print(ErrorMsgUtils.type_error(author, var_type=Author))
            return

        # Validates existence
        book_to_check = self.find_by_name(name)
        if book_to_check is not None:
            print(ErrorMsgUtils.already_exists(name))
            return

        # Validates author existence
        author_db = AuthorDBDAO(db=self.db)
        author_by_id = author_db.find_by_id(author.id)
        if author_by_id is None:
            print(ErrorMsgUtils.does_not_exists(table_name='Author', var=author.id))
            return

        # SQL & Execution
        sql = f"INSERT INTO BOOKS (NAME, PRICE, AUTHOR_ID) VALUES ('{name}', {price}, {author.id})"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
            # Return None
            return None
        else:
            print(self.cursor.rowcount, "was inserted.")
        print("ID: ", self.cursor.lastrowid)
        # Return the Book
        return Book(
            name=name,
            price=price,
            id=self.cursor.lastrowid,
            author_id=author.id
        )

    def find_by_id(self, id):
        """
        Validates ID type is int
        Returns Book by ID if exists
        :param id: int
        :return: Book | None
        """

        # Validates type
        if not TypeUtils.is_type(id, var_type=int):
            print(ErrorMsgUtils.type_error(id, var_type=int))
            return

        # Execution
        sql = f"SELECT * FROM BOOKS WHERE ID = {id}"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            if not results:
                print(ErrorMsgUtils.does_not_exists(table_name='Book', var=id))
                return None

            # Return results
            book_by_id = Book(
                id=results[0],
                name=results[1],
                price=results[2],
                author_id=results[3],
            )
            return book_by_id

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def find_by_name(self, name):
        """
        Validates Name type is str
        :param name: str
        :return: Book | None
        """

        # Validates type
        if not TypeUtils.is_type(name, var_type=str):
            print(ErrorMsgUtils.type_error(name, var_type=str))
            return

        # Execution
        sql = f"SELECT * FROM BOOKS WHERE NAME = '{name}'"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            if not results:
                print(ErrorMsgUtils.does_not_exists(table_name='Book', var=name))
                return None

            # Returns results
            book_by_name = Book(
                id=results[0],
                name=results[1],
                price=results[2],
                author_id=results[3])
            return book_by_name

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def update_book(self, book):
        """
        Validates Book type is Book
        :param book: Book
        :return: Updated Book | None
        """

        # Validates type
        if not TypeUtils.is_type(book, var_type=Book):
            print(ErrorMsgUtils.type_error(book, var_type=Book))
            return

        # Execution
        sql = f"UPDATE BOOKS SET NAME = '{book.name}', " \
              f"PRICE = '{book.price}' " \
              f"WHERE ID = {book.id}"
        try:
            self.cursor.execute(sql)
            self.db.commit()

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
            return None
        else:

            # Return updated Book
            print(self.cursor.rowcount, "was updated.")
            updated_book = self.find_by_id(book.id)
            return updated_book

    def remove_book(self, id):
        """
        Validates ID type is int
        Validates existence before removing
        Delete Book and returns it
        :param id: int
        :return: Deleted Book | None
        """

        # Validates type
        if not TypeUtils.is_type(id, var_type=int):
            print(ErrorMsgUtils.type_error(id, var_type=int))
            return

        # Validates existence
        book = self.find_by_id(id)
        if not book:
            return

        # Execution
        sql = f"DELETE FROM BOOKS WHERE ID = {id}"

        try:
            self.cursor.execute(sql)
            self.db.commit()

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
        else:

            # Returns Deleted Book
            print(self.cursor.rowcount, "was deleted.")
            return book

    def find_all(self):
        """
        Returns all Books
        :param self:
        :return: List of Books
        """

        try:
            # Execution
            sql = "SELECT * FROM BOOKS"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()

            # No Data
            if not results:
                print(ErrorMsgUtils.no_data_available())
                return

            # Return results
            return results

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
