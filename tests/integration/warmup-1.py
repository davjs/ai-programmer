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
        self.failUnlessEqual(function.execute(["False", "False"]), True)
        self.failUnlessEqual(function.execute(["True", "False"]), False)
        self.failUnlessEqual(function.execute(["False", "True"]), True)

    def testMonkeyTrouble(self):
        function = Function("monkey_trouble", [Parameter("a_smile", bool), Parameter("b_smile", bool)], int)
        function.add_requirement(Requirement((True, True), True))
        function.add_requirement(Requirement((False, False), True))
        function.add_requirement(Requirement((True, False), False))
        function.add_requirement(Requirement((False, True), False))
        programmer.write(function)
        self.failUnlessEqual(function.execute(["True", "True"]), True)
        self.failUnlessEqual(function.execute(["False", "False"]), True)
        self.failUnlessEqual(function.execute(["True", "False"]), False)
        self.failUnlessEqual(function.execute(["False", "True"]), False)

    def testSumDouble(self):
        function = Function("sum_double", [Parameter("a", int), Parameter("b", int)], int)
        function.add_requirement(Requirement((1, 2), 3))
        function.add_requirement(Requirement((3, 2), 5))
        function.add_requirement(Requirement((2, 2), 8))
        function.add_requirement(Requirement((3, 3), 12))
        programmer.write(function)
        self.failUnlessEqual(function.execute(["1", "2"]), 3)
        self.failUnlessEqual(function.execute(["3", "2"]), 5)
        self.failUnlessEqual(function.execute(["2", "2"]), 8)
        self.failUnlessEqual(function.execute(["3", "3"]), 12)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
