from sympy import *

__author__ = 'David'


def get_boolean_equation(boolean_var_names: list, requirements: list):
    if len(requirements) > 1:
        true_parameters = [list(r.parameters) for r in requirements if r.output]
        false_parameters = []  # [list(r.parameters) for r in requirements if r.output == False]
        formula = SOPform(boolean_var_names, true_parameters, false_parameters)
        print(formula)
        return "return " + render_formula(formula, True)

def render_formula(formula, first=False):
    text = ''

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