from main.function import Function, Requirement
from main.programgenerator2 import Parameter

__author__ = 'david'

import unittest
from main import programmer

class WarmupTests(unittest.TestCase):

    def testSleepIn(self):
        function = Function("sleep_in", [Parameter("weekday", bool), Parameter("vacation", bool)], int)
        function.add_requirement(Requirement((False, False), True))
        function.add_requirement(Requirement((True, False), False))
        function.add_requirement(Requirement((False, True), True))
        programmer.write(function)
        self.failUnless(function.execute(["False", "False"]) == True)
        self.failUnless(function.execute(["True", "False"]) == False)
        self.failUnless(function.execute(["False", "True"]) == True)

    def testMonkeyTrouble(self):
        function = Function("monkey_trouble", [Parameter("a_smile", bool), Parameter("b_smile", bool)], int)
        function.add_requirement(Requirement((True, True), True))
        function.add_requirement(Requirement((False, False), True))
        function.add_requirement(Requirement((True, False), False))
        function.add_requirement(Requirement((False, True), False))
        programmer.write(function)
        self.failUnless(function.execute(["True", "True"]) == True)
        self.failUnless(function.execute(["False", "False"]) == True)
        self.failUnless(function.execute(["True", "False"]) == False)
        self.failUnless(function.execute(["False", "True"]) == False)



def main():
    unittest.main()

if __name__ == '__main__':
    main()