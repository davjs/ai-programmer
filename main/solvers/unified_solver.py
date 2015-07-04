from main.solvers.math_solver import get_linear_equation

__author__ = 'david'

def solve_boolean_equation(int_var: str, requirements: list):
    eq = get_linear_equation(int_var, requirements, interpolate=False)
    success_expressions = []
    if len(eq) % 2 == 0:
        for line_nr in range(0, len(eq)-1, 2):
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

def solver_mixed_equation(int_var: str,bool_var:str, requirements:list):
    success_reqs = [req.parameters for req in requirements if req.output == True]
