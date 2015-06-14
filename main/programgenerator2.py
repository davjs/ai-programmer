__author__ = 'David'
from enum import Enum


class PROGRAM_INTENTION(Enum):
    reduce_list = 0
    modify_list = 1
    modify_integer_by_constant = 2


class Parameter:
    variable_name = ''
    variable_type = None

    def __init__(self, variable_name: str, variable_type):
        self.variable_type = variable_type
        self.variable_name = variable_name

class ProgramGenerator2:
    parameters = []
    numbers = ("0", "1", "2", "3", "5")
    arithmetic_operators = ("+", "-", "*")
    comparison_operators = ("==", "<", ">")
    assignment = "="
    length = 0
    resulting_type = type(None)

    def __init__(self, parameters: list, resulting_type):
        self.data = []
        self.parameters = parameters
        self.resulting_type = resulting_type
        self.intention = self.get_program_intention()

    def get_program_intention(self) -> PROGRAM_INTENTION:
        _type = self.parameters[0].variable_type
        if len(self.parameters) == 1:
            if _type is list:
                if self.resulting_type is int:
                    return PROGRAM_INTENTION.reduce_list
            if _type is int:
                if self.resulting_type is int:
                    # TODO: This feature might be a bit to specific and unnecessary
                    return PROGRAM_INTENTION.modify_integer_by_constant

    def reduce_list_programs(self, list_name: str):
        for expr in self.get_computed_expressions_using_both_variables("y", "i"):
            yield ["y = 0\n",  # Init something
                   "for i in " + list_name + ":\n",  # loop list
                   "\ty = " + expr + "\n",
                   "return y"]  # return something accumulated from the loop

    def get_codes(self, lines_of_code: int) -> list:  # list[str]
        # TODO: Change to some mapping from enum->func
        if self.intention == PROGRAM_INTENTION.reduce_list:
            list_var = self.parameters[0].variable_name
            return [''.join(program) for program in self.reduce_list_programs(list_var)]
        if self.intention == PROGRAM_INTENTION.modify_integer_by_constant:
            int_var = self.parameters[0].variable_name
            return [''.join(program) for program in self.modify_int_programs(int_var)]
        else:
            raise Exception("Unknown intention")

    def get_computed_expressions_using_both_variables(self, param1, param2) -> list:
        addition = param1 + ' + ' + param2
        multiply = param1 + ' * ' + param2
        minus = [value1 + ' - ' + value2
                 for value1 in [param1, param2]
                 for value2 in [param1, param2]]
        return minus + [multiply, addition]

    def modify_int_programs(self, int_var):
        raise Exception("Not yet implemented")
