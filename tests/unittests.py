__author__ = 'david'

import unittest
from main import programmer



class programmerTest(unittest.TestCase):

    def testSimpleReq(self):
        requirements = []
        function = programmer.makeFunction("foo","x")
        function.addRequirement(5,5)
        programmer.write(function)
        self.failUnless(function.execute("5") == 5)
        print(function.body_text)

    def testTwoReq(self):
        requirements = []
        function = programmer.makeFunction("foo","x")
        function.addRequirement(5,5)
        function.addRequirement(6,6)
        programmer.write(function)
        self.failUnless(function.execute("5") == 5)
        self.failUnless(function.execute("6") == 6)
        print(function.body_text)

    def testDiffReqAndAsserts(self):
        requirements = []
        function = programmer.makeFunction("foo","x")
        function.addRequirement(5,6)
        function.addRequirement(6,7)
        function.addRequirement(7,8)
        programmer.write(function)
        self.failUnless(function.execute("4") == 5)
        self.failUnless(function.execute("5") == 6)
        print(function.body_text)

def main():
    unittest.main()

if __name__ == '__main__':
    main()