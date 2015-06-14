from main.function import Function
from main.programgenerator2 import ProgramGenerator2

__author__ = 'david'

def write(function : Function):
    generator = ProgramGenerator2(function.parameters, function.resulting_type)
    for number_of_lines in range(1,4):
        for code in generator.get_codes(number_of_lines):
            function.body_text = code  # OLD: render_program(statement)
            works = True
            for req in function.requirements:
                try:
                    if function.execute(str(req[0])) != req[1]:
                        works = False
                        break
                except:
                    works = False
                    break
            if works:
                return
    assert False

def render_program(tokens):
    return ' '.join(tokens) + "\n"
