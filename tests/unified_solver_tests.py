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
        requirements = [Requirement((1, 1), 1),
                        Requirement((2, 1), 1),
                        Requirement((3, 1), 0),
                        Requirement((4, 1), 0),

                        Requirement((1, 0), 0),
                        Requirement((2, 0), 0),
                        Requirement((3, 0), 0),
                        Requirement((4, 0), 0)]
        eq = solver_mixed_equation("numb", "switch", requirements)
        self.failUnlessEqual("not x >= 6 and x >= 4", eq)

        # return Talking and hour < 7

        #talking true:
        #true,6 true
        #true,7 true