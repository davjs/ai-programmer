from main.programgenerator2 import PROGRAM_INTENTION, Parameter

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

    def test_get_intention(self):
        generator = programgenerator2.ProgramGenerator2([Parameter("list_to_sum", type([]))], type(0))
        self.failUnless(generator.intention == PROGRAM_INTENTION.reduce_list)

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
        generator = programgenerator2.ProgramGenerator2([Parameter("list_to_sum", type(list))], type(int))
        self.failUnless("y + i" in generator.get_computed_expressions_using_both_variables("y", "i"))
