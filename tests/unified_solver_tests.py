from main.function import Requirement
from main.solvers.unified_solver import solve_boolean_equation, solver_mixed_equation

__author__ = 'david'

import unittest


class MathSolverTests(unittest.TestCase):

    def testBoolFromIntLargerEqualThan(self):
        requirements = [Requirement((1,), 0),
                        Requirement((2,), 0),
                        Requirement((3,), 0),
                        Requirement((4,), 1),
                        Requirement((5,), 1)]
        eq = solve_boolean_equation("x", requirements)
        self.failUnlessEqual("x >= 4", eq)

    def testBoolFromIntLessThan(self):
        requirements = [Requirement((1,), 1),
                        Requirement((2,), 1),
                        Requirement((3,), 1),
                        Requirement((4,), 0),
                        Requirement((5,), 0)]
        eq = solve_boolean_equation("x", requirements)
        self.failUnlessEqual("not x >= 4", eq)

    def testBoolFromIntLargerEqualAndLessThan(self):
        requirements = [Requirement((1,), 0),
                        Requirement((2,), 0),
                        Requirement((3,), 0),
                        Requirement((4,), 1),
                        Requirement((5,), 1),
                        Requirement((6,), 0),
                        Requirement((7,), 0)]
        eq = solve_boolean_equation("x", requirements)
        self.failUnlessEqual("not x >= 6 and x >= 4", eq)

    def testBoolFromIntAndBool(self):
        requirements = [Requirement((1, 1), 0),
                        Requirement((2, 1), 0),
                        Requirement((3, 1), 1),
                        Requirement((4, 1), 1),

                        Requirement((1, 0), 0),
                        Requirement((2, 0), 0),
                        Requirement((3, 0), 0),
                        Requirement((4, 0), 0)]
        eq = solver_mixed_equation("numb", ["switch", ], requirements)
        self.failUnlessEqual("switch and numb >= 3", eq)

    def testParrotTrouble(self):
        requirements = [Requirement((5, True), True),
                        Requirement((6, True), True),
                        Requirement((7, True), False),
                        Requirement((6, False), False),
                        Requirement((21, True), True),
                        Requirement((23, True), True)]
        eq = solver_mixed_equation("hour", ["talking", ], requirements)
        self.failUnlessEqual("talking and (hour < 7 or hour > 20)", eq)

        # return talking and (hour < 7 or hour > 20)

        # talking true:
        # true,6 true
        # true,7 true
