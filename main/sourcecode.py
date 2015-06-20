__author__ = 'david'


class SourceCode:
    source_lines = ()

    def __init__(self, code: tuple):
        self.source_lines = code

    def get_code(self):
        return self.source_lines

    def is_valid(self):
        return not self.source_lines[- 1].startswith("for")

    def auto_indent(self):
        to_indent = []

        for index, line_of_code in enumerate(self.source_lines):
            if line_of_code.startswith("for"):
                to_indent.append(index + 1)

        if len(to_indent) > 0:
            lst = list(self.source_lines)
            for index in to_indent:
                lst[index] = "\t" + lst[index]
            self.source_lines = tuple(lst)


'''
class SourceCodes:
    programs = []

    def __init__(self, programs: list):
        self.programs = programs
'''
