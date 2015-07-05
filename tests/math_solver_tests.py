from main.function import Requirement
from main.solvers.math_solver import get_linear_equation
from main.solvers.unified_solver import solve_boolean_equation

__author__ = 'david'

import unittest


class MathSolverTests(unittest.TestCase):
    def testLinearEquationXTimes2(self):
        requirements = [Requirement((1,), 2),
                        Requirement((2,), 4),
                        Requirement((3,), 6)]
        eq = get_linear_equation("x", requirements)
        self.failUnlessEqual(["return x * 2"], eq)

    def testLinearEquationDiff21(self):
        requirements = [Requirement((19,), 2),
                        Requirement((10,), 11),
                        Requirement((21,), 0)]
        eq = get_linear_equation("n", requirements)
        self.failUnlessEqual(["return n * -1 + 21"], eq)

    def testLinearEquationDiff21OrDouble(self):
        requirements = [Requirement((19,), 2),
                        Requirement((10,), 11),
                        Requirement((21,), 0),
                        Requirement((22,), 2)
                        ]
        eq = get_linear_equation("n", requirements)
        self.failUnlessEqual(
            ["if n >= 21:",
             "\treturn n * 2 + -42",
             "else:",
             "\treturn n * -1 + 21"], eq)

    def testBoolFromIntLessThan(self):
        requirements = [Requirement((1,), 1),
                        Requirement((2,), 1),
                        Requirement((3,), 1),
                        Requirement((4,), 0),
                        Requirement((5,), 0),
                        Requirement((6,), 0)]
        eq = solve_boolean_equation("x", requirements)
        self.failUnlessEqual("not x >= 4", eq)

    # False,False,False,True,True,True
    # return x >= 4

    def testNoInterpolate(self):
        requirements = [Requirement((0,), 0),
                        Requirement((5,), 10),
                        Requirement((10,), 20),
                        Requirement((15,), 15),
                        Requirement((20,), 15)]
        eq = get_linear_equation("x", requirements, interpolate=False)
        self.failUnlessEqual(["if x >= 15:",
                              "\treturn 15",
                              "else:",
                              "\treturn x * 2"], eq)

    # The integer part of the parrot trouble program, ie (hour < 7 or hour > 20)
    def test_parrot_int_part(self):
        requirements = [Requirement((5,), 1),
                        Requirement((6,), 1),
                        Requirement((7,), 0),
                        Requirement((8,), 0),
                        Requirement((21,), 1),
                        Requirement((23,), 1)]
        eq = get_linear_equation("hour", requirements)
        self.failUnlessEqual(["if hour >= 21:",
                              "\treturn 1",
                              "if not hour >= 7:",
                              "\treturn 1"
                              "else:"
                              "\treturn 0"], eq)

        """ ALTERNATIVE:
        self.failUnlessEqual(["if hour >= 21:",
                                "return 1",
                              "if hour >= 7:",
                                "return 0"
                              "else:"
                                "return 1"], eq)"""


def main():
    unittest.main()


if __name__ == '__main__':
    main()
