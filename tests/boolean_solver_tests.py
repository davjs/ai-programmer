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


# 1    2    3     4    5    6
# False,True,False,True,False,True
# return x % 2

# True,True,True,False,False,False
# return x < 4




# True,True,False,False,False,True
# return x >= 3 and x <= 4


def main():
    unittest.main()


if __name__ == '__main__':
    main()
