import itertools

from main.sourcecode import SourceCode

__author__ = 'david'


class ProgramGenerator:
    parameters = ()
    numbers = ("0", "1", "2", "3", "5")
    arithmetic_operators = ("+", "-", "*")
    comparison_operators = ("==", "<", ">")
    assignment = "="
    length = 0

    def __init__(self, *parameters: tuple, length: int):
        self.length = length
        self.data = []
        self.parameters = parameters

    def get_variables(self):
        return self.parameters + ("y", "i")  # TODO: + variables

    def get_values(self):
        return self.numbers + self.get_variables()

    def get_computed_values(self):
        return tuple(value1 + ' ' + operator + ' ' + value2
                     for value1 in self.get_variables()  # only non const
                     for value2 in self.get_values()  # any value
                     for operator in self.arithmetic_operators
                     if not (operator == "*" and value2 == "1")  # x*1
                     and not (operator == "-" and value1 == value2)  # x-x
                     )

    def get_expressions(self):
        return self.get_values() + self.get_computed_values()

    def get_assignments(self):
        return tuple(value1 + ' ' + '=' + ' ' + value2
                     for value1 in self.get_variables()  # only non const
                     for value2 in self.get_expressions()  # any value
                     if not value1 == value2)  # x*1

    @staticmethod
    def get_operational_function_calls():
        return ()

    def get_operations(self):
        return self.get_assignments() + self.get_operational_function_calls()

    def get_returns(self):
        return ['return ' + str(expr) for expr in self.get_expressions()]

    def get_for_loops(self):
        return tuple('for i in ' + str(expr) + ':' for expr in self.parameters)

    @staticmethod
    def fix_indentation(source_codes: list) -> list:
        for code in source_codes:
            code.auto_indent()
        return source_codes

    def get_statement_pairs(self, number_of_lines: int):
        assert number_of_lines > 0
        #  we only fit return if one line
        if number_of_lines == 1:
            return self.get_returns()
        else:
            # operation|loop|return|break
            self.get_for_loops()
            operations = self.get_operations() + self.get_for_loops()
            op_list = [operations for ops in range(number_of_lines - 1)]
            programs = itertools.product(*op_list)
            source_codes = [SourceCode(text) for text in programs]
            source_codes = [code for code in source_codes if code.is_valid()]
            source_codes = self.fix_indentation(source_codes)
            # Operations + return
            return ['\n'.join(oper.get_code()) + "\n" + ret for oper in source_codes for ret in self.get_returns()]

    def get_codes(self, length: int):
        return self.get_statement_pairs(length)
