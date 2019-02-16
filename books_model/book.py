from utils.utils import TypeUtils
from utils.utils import ErrorMsgUtils


class Book:

    def __init__(self, name, author_id=None, price=0, id=None):
        self.__name = name
        self.__author_id = author_id
        self.__price = price
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):

        # Validates type
        if not TypeUtils.is_type(new_id, var_type=int):
            print(ErrorMsgUtils.type_error(new_id, var_type=int))
            return

        # Validates legal value
        if new_id < 1:
            print(ErrorMsgUtils.illegal_value(new_id))
            return

        # Set value
        self.__id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        # Validates type
        if not TypeUtils.is_type(new_name, var_type=str):
            print(ErrorMsgUtils.type_error(new_name, var_type=str))
            return

            # Validates legal value
        if not new_name:
            print(ErrorMsgUtils.illegal_value(new_name))
            return

        # Set value
        self.__name = new_name

    @property
    def author_id(self):
        return self.__author_id

    @author_id.setter
    def author_id(self, new_author):
        # Validates type
        if not TypeUtils.is_type(new_author, var_type=int):
            print(ErrorMsgUtils.type_error(new_author, var_type=int))
            return
        # Set value
        self.__author_id = new_author


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        # Validates type
        if not TypeUtils.is_type_or(new_price, var_type1=int, var_type2=float):
            print(ErrorMsgUtils.none_of_type(int, float, var=new_price))
            return

        # Validates legal value
        if new_price <= 0:
            print(ErrorMsgUtils.illegal_value(new_price))
            return

        # Set value
        self.__price = new_price

    def __str__(self):
        return f"Book: (ID: {self.id}, Name: {self.name}, Price: {self.price}, Author's ID: {self.author_id})"
