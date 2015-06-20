from main.sourcecode import SourceCode

__author__ = 'david'

import unittest
from main import programgenerator


class GeneratorTests(unittest.TestCase):
    # SIMPLE X EXPRESSIONS

    def testExpressionX(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("x" in generator.get_expressions())

    def testExpressionXPlus1(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("x + 1" in generator.get_expressions())

    # SIMPLE RETURN STATEMENTS

    def testStatementReturn1(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("return 1" in generator.get_returns())

    def testStatementReturnX(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("return x" in generator.get_returns())

    def testStatementReturnXPlus1(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("return x + 1" in generator.get_returns())

    def testStatementReturnXTimes2(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("return x * 2" in generator.get_returns())

    # ASSIGNMENT OEPRATIONS

    def testOperationAssign1ToY(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("y = 1" in generator.get_assignments())
        print(generator.get_assignments())

    # FOR LOOPS

    def testForIInList(self):
        generator = programgenerator.ProgramGenerator("list_of_numbers", length=1)
        self.failUnless("for i in list_of_numbers:" in generator.get_for_loops())

    # FIX INDENTATION

    def testFixIndentation(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        source_codes = generator.fix_indentation([SourceCode(("1", "for", "3", "4")),
                                                  SourceCode(("1", '2', 'for', '4'))])
        self.failUnlessEqual(source_codes[0].get_code(), ('1', 'for', '\t3', '4'))
        self.failUnlessEqual(source_codes[1].get_code(), ('1', '2', 'for', '\t4'))

    # MULTILINE TESTS

    def testAssign1ToYReturnY(self):
        generator = programgenerator.ProgramGenerator("x", length=1)
        self.failUnless("y = 1\n"
                        "return y" in generator.get_codes(2))

    # posibly unwanted
    # def testAssignXplusXToYReturnY(self):
    #   generator = programgenerator.programgenerator("x", length=1)
    #   self.failUnless("y = x + x" in generator.get_operations())
    #   self.failUnless("y = x + x\n" +
    #       "return y" in generator.get_codes(2))

    def testSum(self):
        generator = programgenerator.ProgramGenerator("list_of_numbers", length=1)
        self.failUnless("y = 0" in generator.get_operations())
        self.failUnless("for i in list_of_numbers:" in generator.get_for_loops())
        self.failUnless("y = y + i" in generator.get_operations())

        self.failUnless(any("y = y + i" in codes for codes in generator.get_codes(3)))

        # self.failUnless("y = 0\n" +
        #                "for i in list_of_numbers:\n" +
        #                "\t y = y + i\n" +
        #                "return y" in generator.get_codes(4))
