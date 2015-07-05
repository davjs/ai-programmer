from main.function import Requirement
from main.solvers.boolean_solver import solve_boolean_expression
from main.solvers.math_solver import get_linear_equation

__author__ = 'david'


def solve_boolean_equation(int_var: str, requirements: list):
    eq = get_linear_equation(int_var, requirements, interpolate=False)
    success_expressions = []
    if len(eq) % 2 == 0:
        for line_nr in range(0, len(eq) - 1, 2):
            if_statement = eq[line_nr]
            if "else" in if_statement:
                break
            return_statement = eq[line_nr + 1]
            if "1" in return_statement:
                success_expressions.append(if_statement[3:-1])
            else:
                success_expressions.append("not " + if_statement[3:-1])
        return " and ".join(success_expressions)
    return eq


def solver_mixed_equation(int_var: str, bool_vars: list, requirements:list):
    bool_reqs = [Requirement(req.parameters[1:], req.output) for req in requirements]

    bool_eq = solve_boolean_expression(bool_vars, bool_reqs)
    true_by_boolean_definition = []
    for req in requirements:
        for var_value, var_name in zip(req.parameters[1:], bool_vars):
            new_eq = bool_eq.replace(var_name, str(var_value))
            print(new_eq)
            if eval(new_eq):
                true_by_boolean_definition.append(req)
    return bool_eq + " and " + solve_boolean_equation(int_var, true_by_boolean_definition)
