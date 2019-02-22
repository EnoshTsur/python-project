from utils.utils import ErrorMsgUtils
from utils.utils import TypeUtils
from author_model.author import Author
import mysql.connector


class AuthorDBDAO:

    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def create_table(self):
        """
        Create Books Table
        :return:
        """
        try:
            self.cursor.execute("CREATE TABLE AUTHOR "
                                "(ID INT AUTO_INCREMENT PRIMARY KEY, "
                                "FIRST_NAME VARCHAR(255), "
                                "LAST_NAME VARCHAR(255)"
                                ")")
            # Success
            print("Table Author was created successfully")

            # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def create_author(self, first_name, last_name):
        """
        Validates type first_name & last_name is str
        Validates author does not exists by first & last name
        :param first_name: str
        :param last_name: str
        :return: Author | None
        """

        # Validates type
        if not TypeUtils.all_of_type(first_name, last_name, var_type=str):
            print(ErrorMsgUtils.type_error(first_name, last_name, var_type=str))
            return

        # Validate existence
        author_to_check = self.find_by_name(first_name, last_name)
        if author_to_check is not None:
            print(ErrorMsgUtils.already_exists(f"{first_name}-{last_name}"))
            return

        sql = f"INSERT INTO AUTHOR(FIRST_NAME, LAST_NAME) VALUES ('{first_name}', '{last_name}')"
        # Execution
        try:
            self.cursor.execute(sql)
            self.db.commit()

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
        else:
            print(self.cursor.rowcount, "was inserted.")
            print("ID: ", self.cursor.lastrowid)
            # Return the Book
            return Author(
                first_name=first_name,
                last_name=last_name,
                id=self.cursor.lastrowid
            )

    def find_by_name(self, first_name, last_name):
        """
        Validates first_name & last_name are str
        Returns Author if exists
        :param first_name: str
        :param last_name: str
        :return: Author | None
        """

        # Validates type
        if not TypeUtils.all_of_type(first_name, last_name, var_type=str):
            print(ErrorMsgUtils.type_error(first_name, last_name, var_type=str))
            return

        # Validate legal value
        if not first_name:
            print(ErrorMsgUtils.illegal_value(first_name))
        if not last_name:
            print(ErrorMsgUtils.illegal_value(last_name))

        sql = f"SELECT * FROM AUTHOR WHERE FIRST_NAME = '{first_name}' AND LAST_NAME = '{last_name}'"
        # Execution
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            if not results:
                print(ErrorMsgUtils.does_not_exists(table_name='Author', var=f"{first_name}, {last_name}"))
                return

            # Return results
            return Author(
                id=results[0],
                first_name=results[1],
                last_name=results[2]
            )

        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def find_by_id(self, id):
        """
        Validate ID type is int
        Returns Author if exists
        :param id: int
        :return: Author | None
        """

        # Validate type
        if not TypeUtils.is_type(id, var_type=int):
            print(ErrorMsgUtils.type_error(id, var_type=int))
            return

        sql = f"SELECT * FROM AUTHOR WHERE ID = {id}"
        # Execution
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            if not results:
                print(ErrorMsgUtils.does_not_exists(table_name='Author', var=id))
                return

            # Return results
            return Author(
                id=results[0],
                first_name=results[1],
                last_name=results[2]
            )

        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def update_author(self, author):
        """
        Validates author type is Author
        :param author: Author
        :return: Updated Author | None
        """

        # Validate type
        if not TypeUtils.is_type(author, var_type=Author):
            print(ErrorMsgUtils.type_error(author, var_type=Author))
            return

        sql = f"UPDATE AUTHOR SET " \
              f"FIRST_NAME = '{author.first_name}', " \
              f"LAST_NAME = '{author.last_name}' " \
              f"WHERE ID = {author.id}"

        # Execution
        try:
            self.cursor.execute(sql)
            self.db.commit()
        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
            return
        else:
            # Return updated results
            return self.find_by_id(author.id)

    def remove_author(self, id):
        """
        Validates id type is int
        Validates existence before removing
        Removing & returns the removed row
        :param id:
        :return:
        """

        # Validates type
        if not TypeUtils.is_type(id, var_type=int):
            print(ErrorMsgUtils.type_error(id, var_type=int))
            return

        # Validate existence
        author = self.find_by_id(id)
        if author is None:
            return

        sql = f"DELETE FROM AUTHOR WHERE ID = {id}"
        # Execution
        try:
            self.cursor.execute(sql)
            self.db.commit()

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))
        else:
            return author

    def find_all(self):
        """
        Returns all authors or none
        :return: List of Authors | None
        """

        sql = "SELECT * FROM AUTHOR"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            # No Data case
            if not results:
                print(ErrorMsgUtils.no_data_available())
                return

            # Return results
            return results

        # Error
        except mysql.connector.Error as error:
            print(ErrorMsgUtils.display_error(error))

    def find_authors_books(self, author_id):
        """
        Validates author_id type is int
        Returns all authors books
        :param author_id: int
        :return: List of Books | None
        """

        # Validates type
        if not TypeUtils.is_type(author_id, var_type=int):
            print(ErrorMsgUtils.type_error(author_id, var_type=int))
            return

        sql = f"SELECT BOOKS.* FROM AUTHOR, BOOKS " \
              f"WHERE AUTHOR.ID = {author_id} AND BOOKS.AUTHOR_ID = {author_id}"
        # Execution
        try:
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
