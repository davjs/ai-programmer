from main.function import Function
from main.programgenerator2 import ProgramGenerator2

__author__ = 'david'


def write(function: Function):
    generator = ProgramGenerator2(function.parameters, function.resulting_type)
    for number_of_lines in range(1, 4):
        programs = [render_program(tokens) for tokens in generator.get_codes(number_of_lines)]
        for program in programs:
            function.body_text = program  # OLD: render_program(statement)
            works = True
            for req in function.requirements:
                # try:
                if function.execute(req.parameters) != req.output:
                    works = False
                    break
                    # except SyntaxError:
                    #    works = False
                    #    break
            if works:
                return
    assert False


def render_program(program):
    return ''.join(['\t' + codeline + '\n' for codeline in program])
