__author__ = 'David'


def get_modified_int(int_var):
    return [int_var, int_var + "+ 1", int_var + "* 2"]


def get_computed_expressions_using_both_variables(param1, param2) -> list:
    addition = param1 + ' + ' + param2
    multiply = param1 + ' * ' + param2
    minus = [value1 + ' - ' + value2
             for value1 in [param1, param2]
             for value2 in [param1, param2]]
    return minus + [multiply, addition]


def get_modified_boolean_expression(bool_var) -> list:
    return [bool_var, "(not " + bool_var + ')']


def get_computed_boolean_expressions_using_all_variables(parameters) -> list:
    if len(parameters) == 2:
        return [b0 + operator + b1
                for b0 in get_modified_boolean_expression(parameters[0])
                for b1 in get_modified_boolean_expression(parameters[1])
                for operator in [" or ", " and ", " == "]]
    else:
        raise Exception("not yet implemented")


def get_boolean_expression_from_ints(parameters) -> list:
    if len(parameters) == 2:
        return [parameters[0] + operator + parameters[1]
                for operator in [" == ", " < ", " > "]]


def get_combined_integers(parameters):
    if len(parameters) == 2:
        return [parameters[0] + operator + parameters[1]
                for operator in ['+', '-', '*']]
    else:
        raise Exception("not yet implemented")
