from nose.tools import assert_equals

from main.function import Requirement
from main.solvers.boolean_solver import solve_boolean_expression

__author__ = 'david'


def testBooleanOr():
    requirements = [Requirement((0, 0), 0),
                    Requirement((0, 1), 1),
                    Requirement((1, 0), 1),
                    Requirement((1, 1), 1)]
    eq = solve_boolean_expression(["x", "y"], requirements)
    assert_equals("x or y", eq)


def testBooleanXor():
    requirements = [Requirement((0, 0), 0),
                    Requirement((0, 1), 1),
                    Requirement((1, 0), 1),
                    Requirement((1, 1), 0)]
    eq = solve_boolean_expression(["x", "y"], requirements)
    assert_equals("(x and not y) or (y and not x)", eq)
