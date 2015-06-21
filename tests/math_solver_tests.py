from main.function import Requirement
from main.math_solver import get_linear_equation

__author__ = 'david'

import unittest


class MathSolverTests(unittest.TestCase):
    def testLinearEquationXTimes2(self):
        requirements = [Requirement((1,), 2),
                        Requirement((2,), 4),
                        Requirement((3,), 6)]
        eq = get_linear_equation(requirements, "x")
        self.failUnlessEqual("return x * 2", eq)

    def testLinearEquationDiff21(self):
        requirements = [Requirement((19,), 2),
                        Requirement((10,), 11),
                        Requirement((21,), 0)]
        eq = get_linear_equation(requirements, "n")
        self.failUnlessEqual("return n * -1 + 21", eq)

    def testLinearEquationDiff21OrDouble(self):
        requirements = [Requirement((19,), 2),
                        Requirement((10,), 11),
                        Requirement((21,), 0),
                        Requirement((22,), 2)
                        ]
        eq = get_linear_equation(requirements, "n")
        self.failUnlessEqual(
            ["if n > 21:",
             "\treturn n * 2 + -42",
             "else:",
             "\treturn n * -1 + 21"], eq)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
