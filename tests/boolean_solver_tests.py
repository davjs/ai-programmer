from main.function import Requirement
from main.solvers.boolean_solver import get_boolean_equation

__author__ = 'david'

import unittest


class BooleanSolverTests(unittest.TestCase):
    def testBooleanOr(self):
        requirements = [Requirement((0, 0), 0),
                        Requirement((0, 1), 1),
                        Requirement((1, 0), 1),
                        Requirement((1, 1), 1)]
        eq = get_boolean_equation(["x", "y"], requirements)
        self.failUnlessEqual("x or y", eq)

    def testBooleanXor(self):
        requirements = [Requirement((0, 0), 0),
                        Requirement((0, 1), 1),
                        Requirement((1, 0), 1),
                        Requirement((1, 1), 0)]
        eq = get_boolean_equation(["x", "y"], requirements)
        print(eq)
        self.failUnlessEqual("(x and not y) or (y and not x)", eq)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
