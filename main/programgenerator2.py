import types

__author__ = 'David'
from enum import Enum


class PROGRAM_INTENTION(Enum):
    reduce_list = 0
    modify_list = 1
    modify_integer_by_constant = 2
    combine_booleans = 3


class Parameter:
    variable_name = ''
    variable_type = None

    def __init__(self, variable_name: str, variable_type: type):
        self.variable_type = variable_type
        self.variable_name = variable_name


def get_computed_expressions_using_single_variable(int_var):
    return [int_var, int_var + "+ 1"]


def modify_int_programs(int_var):
    for expr in get_computed_expressions_using_single_variable(int_var):
        yield ["return " + expr]  # return some modification to the variable


def get_computed_expressions_using_both_variables(param1, param2) -> list:
    addition = param1 + ' + ' + param2
    multiply = param1 + ' * ' + param2
    minus = [value1 + ' - ' + value2
             for value1 in [param1, param2]
             for value2 in [param1, param2]]
    return minus + [multiply, addition]

def get_modified_boolean_expression(bool_var) -> list:
    return [bool_var, "not " + bool_var]

def get_computed_boolean_expressions_using_all_variables(parameters) -> list:
    if len(parameters) == 2:
        return [b0 + operator + b1
                for b0 in get_modified_boolean_expression(parameters[0])
                for b1 in get_modified_boolean_expression(parameters[1])
                for operator in [" or ", " and ", " == "]]
    else:
        raise Exception("not yet implemented")


def reduce_list_programs(list_name: str):
    for expr in get_computed_expressions_using_both_variables("y", "i"):
        yield ["y = 0\n",  # Init something
               "for i in " + list_name + ":\n",  # loop list
               "\ty = " + expr + "\n",
               "return y"]  # return something accumulated from the loop


def combine_booleans_programs(parameters: list):
    for expr in get_computed_boolean_expressions_using_all_variables(parameters):
        yield ["return " + expr]


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
        elif all(param.variable_type is bool for param in self.parameters):
            return PROGRAM_INTENTION.combine_booleans
        else:
            raise Exception("Unknown intention based on parameters")

    def get_codes(self, lines_of_code: int) -> list:  # list[str]
        # TODO: Change to some mapping from enum->func?
        var1 = self.parameters[0].variable_name

        if self.intention == PROGRAM_INTENTION.reduce_list:
            generator = reduce_list_programs(var1)
        elif self.intention == PROGRAM_INTENTION.modify_integer_by_constant:
            generator = modify_int_programs(var1)
        elif self.intention == PROGRAM_INTENTION.combine_booleans:
            generator = combine_booleans_programs([param.variable_name for param in self.parameters])
        else:
            raise Exception("Intention found but not yet implemented")

        return [''.join(program) for program in generator]
