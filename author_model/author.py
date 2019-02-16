from utils.utils import TypeUtils
from utils.utils import ErrorMsgUtils


class Author:

    def __init__(self, first_name, last_name, id=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_name):
        # Validates type
        if not TypeUtils.is_type(new_name, var_type=str):
            print(ErrorMsgUtils.type_error(new_name, var_type=str))
            return

        # Validates legal value
        if not new_name:
            print(ErrorMsgUtils.illegal_value(new_name))
            return

        # Set name
        self.first_name = new_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_name):
        # Validates type
        if not TypeUtils.is_type(new_name, var_type=str):
            print(ErrorMsgUtils.type_error(new_name, var_type=str))
            return

            # Validates legal value
        if not new_name:
            print(ErrorMsgUtils.illegal_value(new_name))
            return

            # Set name
        self.first_name = new_name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        # Validates type
        if not TypeUtils.is_type(new_id, var_type=int):
            print(ErrorMsgUtils.type_error(new_id, var_type=int))
            return

        # Validate legal value
        if new_id < 1:
            print(ErrorMsgUtils.illegal_value(new_id))
            return

        # Set value
        self.__id = new_id

    def __str__(self):
        return f"Author (ID: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name})"
