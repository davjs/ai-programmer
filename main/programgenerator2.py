from main.solvers import math_solver
from main.expressions import get_modified_int, get_computed_expressions_using_both_variables, \
    get_boolean_expression_from_ints, get_combined_integers
from main.function import Function
from main.solvers.boolean_solver import get_boolean_equation

__author__ = 'David'
from enum import Enum


class ProgramIntention(Enum):
    reduce_list = 0
    modify_list = 1
    modify_integer_by_constant = 2
    combine_booleans = 3
    combine_integers = 4
    bool_from_int = 5


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


def modify_int_programs(int_var, requirements: list):
    equation = math_solver.get_linear_equation(int_var, requirements)
    if equation:
        return equation
    else:
        return "return " + int_var


def combine_booleans_programs(parameters: list, requirements: list):
    equation = get_boolean_equation(parameters, requirements)
    if equation:
        return equation
    else:
        raise NotImplementedError


def boolean_from_int(parameters: list, requirements: list):
    equation = get_boolean_equation(parameters, requirements)
    if equation:
        return equation
    else:
        raise NotImplementedError


def combine_integers_programs(parameters: list):
    if len(parameters) == 2:
        for expr in get_combined_integers(parameters):
            for expr2 in get_modified_int('s'):
                for expr3 in get_boolean_expression_from_ints(parameters):
                    yield ["s = " + expr,  # TODO: make "assignment function", is this really needed?
                           "if " + expr3 + ":",
                           "\treturn " + expr2,
                           "return s"]


def get_program_intention(function_definition: Function) -> ProgramIntention:
    _type = function_definition.parameters[0].variable_type
    if len(function_definition.parameters) == 1:
        if _type is list:
            if function_definition.resulting_type is int:
                return ProgramIntention.reduce_list
        if _type is int:
            if function_definition.resulting_type is int:
                return ProgramIntention.modify_integer_by_constant
            elif function_definition.resulting_type is bool:
                return ProgramIntention.bool_from_int
            else:
                raise Exception("Unknown intention based on parameters")
    elif all(param.variable_type is bool for param in function_definition.parameters):
        return ProgramIntention.combine_booleans
    elif all(param.variable_type is int for param in function_definition.parameters):
        return ProgramIntention.combine_integers
    else:
        raise Exception("Unknown intention based on parameters")


class ProgramGenerator2:
    parameters = []
    resulting_type = type(None)

    def __init__(self, function_definition: Function):
        self.data = []
        self.parameters = function_definition.parameters
        self.resulting_type = function_definition.resulting_type
        self.intention = get_program_intention(function_definition)
        self.requirements = function_definition.requirements

    def get_codes(self, lines_of_code: int) -> list:  # list[str]
        # TODO: Change to some mapping from enum->func?
        variable_names = [param.variable_name for param in self.parameters]

        if self.intention == ProgramIntention.reduce_list:
            return reduce_list_programs(variable_names[0])

        elif self.intention == ProgramIntention.modify_integer_by_constant:
            return modify_int_programs(variable_names[0], self.requirements)

        elif self.intention == ProgramIntention.combine_booleans:
            return combine_booleans_programs(variable_names, self.requirements)

        elif self.intention == ProgramIntention.combine_integers:
            return combine_integers_programs(variable_names)
        elif self.intention == ProgramIntention.bool_from_int:
            return boolean_from_int(variable_names, self.requirements)

        else:
            raise Exception("Intention: '" + str(self.intention) + "' - found but not yet implemented")
