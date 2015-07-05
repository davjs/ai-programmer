from sympy import *

__author__ = 'David'


def solve_boolean_expression(boolean_var_names: list, requirements: list):
    if len(requirements) > 1:
        true_parameters = [list(r.parameters) for r in requirements if r.output]
        parameters_that_doesnt_matter = []
        formula = SOPform(boolean_var_names, true_parameters, parameters_that_doesnt_matter)
        print(formula)
        return render_formula(formula, True)


def get_boolean_equation(boolean_var_names: list, requirements: list):
    return "return " + solve_boolean_expression(boolean_var_names, requirements)

def render_formula(formula, first=False):
    text = ''

    if isinstance(formula, Symbol):
        return str(formula)

    if formula.func == Not:
        text += 'not ' + render_symbol(formula.args[0])
    else:
        rendered_symbols = [render_symbol(s) for s in formula.args]

        if not first:
            text = '('

        if formula.func == Or:
            text += ' or '.join(rendered_symbols)
        elif formula.func == And:
            text += ' and '.join(rendered_symbols)
        elif formula.func == Symbol:
            text += str(formula.args)
        else:
            raise NotImplementedError(formula.func)

        if not first:
            text += ')'

    return text


def render_symbol(expr):
    if isinstance(expr, Symbol):
        return str(expr)
    else:
        return render_formula(expr)
