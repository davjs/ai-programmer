from main.expressions import get_modified_int, get_computed_expressions_using_both_variables, \
    get_computed_boolean_expressions_using_all_variables, get_boolean_expression_from_ints, get_combined_integers

__author__ = 'David'
from enum import Enum


class ProgramIntention(Enum):
    reduce_list = 0
    modify_list = 1
    modify_integer_by_constant = 2
    combine_booleans = 3
    combine_integers = 4


class Parameter:
    variable_name = ''
    variable_type = None

    def __init__(self, variable_name: str, variable_type: type):
        self.variable_type = variable_type
        self.variable_name = variable_name


def reduce_list_programs(list_name: str):
    for expr in get_computed_expressions_using_both_variables("y", "i"):
        yield ["y = 0",  # Init something
               "for i in " + list_name + ":",  # loop list
               "\ty = " + expr,
               "return y"]  # return something accumulated from the loop


def modify_int_programs(int_var):
    for expr in get_modified_int(int_var):
        yield ["return " + expr]  # return some modification to the variable


def combine_booleans_programs(parameters: list):
    for expr in get_computed_boolean_expressions_using_all_variables(parameters):
        yield ["return " + expr]


def combine_integers_programs(parameters: list):
    if len(parameters) == 2:
        for expr in get_combined_integers(parameters):
            for expr2 in get_modified_int('s'):
                for expr3 in get_boolean_expression_from_ints(parameters):
                    yield ["s = " + expr,  # TODO: make "assignment function", is this really needed?
                           "if " + expr3 + ":",
                           "\treturn " + expr2,
                           "return s"]

class ProgramGenerator2:
    parameters = []
    resulting_type = type(None)

    def __init__(self, parameters: list, resulting_type):
        self.data = []
        self.parameters = parameters
        self.resulting_type = resulting_type
        self.intention = self.get_program_intention()

    def get_program_intention(self) -> ProgramIntention:
        _type = self.parameters[0].variable_type
        if len(self.parameters) == 1:
            if _type is list:
                if self.resulting_type is int:
                    return ProgramIntention.reduce_list
            if _type is int:
                if self.resulting_type is int:
                    # TODO: This feature might be a bit to specific and unnecessary
                    return ProgramIntention.modify_integer_by_constant
        elif all(param.variable_type is bool for param in self.parameters):
            return ProgramIntention.combine_booleans
        elif all(param.variable_type is int for param in self.parameters):
            return ProgramIntention.combine_integers
        else:
            raise Exception("Unknown intention based on parameters")

    def get_codes(self, lines_of_code: int) -> list:  # list[str]
        # TODO: Change to some mapping from enum->func?
        variable_names = [param.variable_name for param in self.parameters]

        if self.intention == ProgramIntention.reduce_list:
            return reduce_list_programs(variable_names[0])

        elif self.intention == ProgramIntention.modify_integer_by_constant:
            return modify_int_programs(variable_names[0])

        elif self.intention == ProgramIntention.combine_booleans:
            return combine_booleans_programs(variable_names)

        elif self.intention == ProgramIntention.combine_integers:
            return combine_integers_programs(variable_names)

        else:
            raise Exception("Intention found but not yet implemented")
