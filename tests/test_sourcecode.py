from unittest import TestCase
from main.sourcecode import SourceCode

__author__ = 'david'


class TestSourceCode(TestCase):

    """ TEST CODE IS VALID """
    def test_valid(self):
        self.failIf(SourceCode(('1', '2', '3', 'for')).is_valid())

    """ TEST AUTO INDENTATION """
    def test_auto_indent(self):
        code = SourceCode(('1', '2', 'for', '4'))
        code2 = SourceCode(('1', 'for', '3', '4'))
        code.auto_indent()
        code2.auto_indent()
        self.failUnlessEqual(code.get_code(), ('1', '2', 'for', '\t4'))
        self.failUnlessEqual(code2.get_code(), ('1', 'for', '\t3', '4'))
