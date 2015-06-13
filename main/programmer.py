from main.function import Function
from main.programgenerator import ProgramGenerator

__author__ = 'david'

def makeFunction(functionName,*arg):
    return Function(functionName,*arg)

def write(function : Function):
    generator = ProgramGenerator(*function.parameters, length=1)
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
