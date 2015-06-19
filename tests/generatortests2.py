from main.programgenerator2 import PROGRAM_INTENTION, Parameter, get_computed_boolean_expressions_using_all_variables

__author__ = 'David'

import unittest
from main import programgenerator2


class generatorTests(unittest.TestCase):
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

    # def testStatementReturn1(self):
    #    generator = programgenerator2.ProgramGenerator("x", length=1)
    #    self.failUnless("return 1" in generator.get_returns())

    def test_get_intention_reduce_list(self):
        generator = programgenerator2.ProgramGenerator2([Parameter("list_to_sum", list)], int)
        self.failUnless(generator.intention == PROGRAM_INTENTION.reduce_list)

    def test_get_intention_combine_booleans(self):
        generator = programgenerator2.ProgramGenerator2([Parameter("x", bool), Parameter("y", bool)], bool)
        self.failUnless(generator.intention == PROGRAM_INTENTION.combine_booleans)

    def testBooleanCombineNotxOrY(self):
        expressions = get_computed_boolean_expressions_using_all_variables(["x", "y"])
        self.failUnless("not x or y" in expressions)

    def testBooleanCombineXEqY(self):
        expressions = get_computed_boolean_expressions_using_all_variables(["x", "y"])
        self.failUnless("x == y" in expressions)

    def testStatementReturn1(self):
        generator = programgenerator2.ProgramGenerator2([Parameter("list_to_sum", list)], int)
        programs = generator.get_codes(4)

        self.failUnless(any("y = y + i\n" in codes for codes in programs))
        self.failUnless(any("for i in list_to_sum:\n" in codes for codes in programs))
        self.failUnless(any("\ty = y + i\n" in codes for codes in programs))
        self.failUnless(any("return y" in codes for codes in programs))

        self.failUnless("y = 0\n" +
                        "for i in list_to_sum:\n" +
                        "\ty = y + i\n" +
                        "return y" in programs)

    def test_get_computed_expressions_using_both_variables_y_plus_i(self):
        generator = programgenerator2
        self.failUnless("y + i" in generator.get_computed_expressions_using_both_variables("y", "i"))
