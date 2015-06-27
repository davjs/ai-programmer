import main.expressions
from main.function import Function
from main.programgenerator2 import ProgramIntention, Parameter
from main.expressions import get_computed_boolean_expressions_using_all_variables

__author__ = 'David'

import unittest
from main import programgenerator2


class GeneratorTests(unittest.TestCase):
    # SIMPLE X EXPRESSIONS
    """
    def testExpressionX(self):
        generator = programgenerator2.ProgramGenerator("x", length=1)
        self.failUnless("x" in generator.get_expressions())

    def testExpressionXPlus1(self):
        generator = programgenerator2.ProgramGenerator("x", length=1)
        self.failUnless("x + 1" in generator.get_expressions())
    """
    # SIMPLE RETURN STATEMENTS

    def test_get_intention_reduce_list(self):
        f = Function("foo", [Parameter("list_to_sum", list)], int)
        generator = programgenerator2.ProgramGenerator2(f)
        self.failUnless(generator.intention == ProgramIntention.reduce_list)

    def test_get_intention_combine_booleans(self):
        f = Function("foo", [Parameter("x", bool), Parameter("y", bool)], bool)
        generator = programgenerator2.ProgramGenerator2(f)
        self.failUnless(generator.intention == ProgramIntention.combine_booleans)

    def testBooleanCombineNotxOrY(self):
        expressions = get_computed_boolean_expressions_using_all_variables(["x", "y"])
        self.failUnless("(not x) or y" in expressions)

    def testBooleanCombineXEqY(self):
        expressions = get_computed_boolean_expressions_using_all_variables(["x", "y"])
        self.failUnless("x == y" in expressions)

    def testStatementReturn1(self):
        f = Function("foo", [Parameter("list_to_sum", list)], int)
        generator = programgenerator2.ProgramGenerator2(f)
        programs = list(generator.get_codes(4))

        self.failUnless(any("y = 0" in codes for codes in programs))
        self.failUnless(any("for i in list_to_sum:" in codes for codes in programs))
        self.failUnless(any("\ty = y + i" in codes for codes in programs))
        self.failUnless(any("return y" in codes for codes in programs))

        self.failUnless(["y = 0",
                         "for i in list_to_sum:",
                         "\ty = y + i",
                         "return y"] in programs)

    def test_get_computed_expressions_using_both_variables_y_plus_i(self):
        generator = programgenerator2
        self.failUnless("y + i" in main.expressions.get_computed_expressions_using_both_variables("y", "i"))
