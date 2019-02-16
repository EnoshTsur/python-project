class TypeUtils:
    """
    Type utils for type validations
    """

    @staticmethod
    def is_type(var, var_type):
        return type(var) is var_type

    @staticmethod
    def all_of_type(*args, var_type):
        for var in args:
            if type(var) is not var_type:
                return False
        return True

    @staticmethod
    def is_type_or(var, var_type1, var_type2):
        return type(var) is var_type1 or type(var) is var_type2


class ErrorMsgUtils:
    """
    Static methods returns a custom error message
    """

    @staticmethod
    def type_error(*args, var_type):
        msg = "Error, "

        if len(args) < 2:
            msg += f"{args[0]} "

        else:
            for arg in args:
                msg += f"{arg}, "

        msg += f"is not {var_type}"
        return msg

    @staticmethod
    def none_of_type(*types, var):
        msg = f'Error, {var} is not '

        for index, type in enumerate(types):

            if index == (len(types)-1):
                msg += f'{type}.'
            else:
                msg += f'{type}, '

        return msg

    @staticmethod
    def illegal_value(var):
        return f"Illegal value: {var}"

    @staticmethod
    def already_exists(var):
        return f'Error, {var} is already exists'

    @staticmethod
    def display_error(error):
        return f"Something went wrong: {error}"

    @staticmethod
    def does_not_exists(table_name, var):
        return f'{table_name} by {var} does not exists'

    @staticmethod
    def no_data_available():
        return 'No data available'