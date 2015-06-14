__author__ = 'David'
from enum import Enum


class PROGRAM_INTENTION(Enum):
    reduce_list = 0
    modify_list = 1


class ProgramGenerator2:
    parameters = []
    numbers = ("0", "1", "2", "3", "5")
    arithmetic_operators = ("+", "-", "*")
    comparison_operators = ("==", "<", ">")
    assignment = "="
    length = 0
    resulting_type = type(int)

    def __init__(self, parameters: list, resulting_type):
        self.data = []
        self.parameters = parameters
        self.resulting_type = resulting_type
        self.intention = self.get_program_intention()

    def get_program_intention(self) -> PROGRAM_INTENTION:
        if len(self.parameters) == 1:
            if self.parameters[0][1] is list:
                if self.resulting_type is int:
                    return PROGRAM_INTENTION.reduce_list

    def reduce_list_programs(self, list_name: str):
        for expr in self.get_computed_expressions_using_both_variables("y", "i"):
            yield ["y = 0\n",  # Init something
                   "for i in " + list_name + ":\n",  # loop list
                   "\ty = " + expr + "\n",
                   "return y"]  # return something accumulated from the loop

    def get_codes(self, lines_of_code: int) -> list:  # list[str]
        if self.intention == PROGRAM_INTENTION.reduce_list:
            list_var = self.parameters[0][0]
            return [''.join(program) for program in self.reduce_list_programs(list_var)]

    def get_computed_expressions_using_both_variables(self, param1, param2) -> list:
        addition = param1 + ' + ' + param2
        multiply = param1 + ' * ' + param2
        minus = [value1 + ' - ' + value2
                 for value1 in [param1, param2]
                 for value2 in [param1, param2]]
        return minus + [multiply, addition]
