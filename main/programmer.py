import types

from main.function import Function
from main.programgenerator2 import ProgramGenerator2

__author__ = 'david'


def write(function: Function):
    generator = ProgramGenerator2(function)
    for number_of_lines in range(1, 4):
        codes = generator.get_codes(number_of_lines)
        # TODO: make work even if we only get one program
        programs = render_programs(codes)
        for program in programs:
            function.body_text = program  # OLD: render_program(statement)
            works = True
            for req in function.requirements:
                if function.execute(req.parameters) != req.output:
                    works = False
                    break
            if works:
                return
    assert False


# TODO: Refactor to program / sourcecode class
def render_programs(programs):
    # ONE SINGLE-LINE PROGRAM

    if type(programs) is str:
        return ['\t' + programs + '\n']

    elif type(programs) is list or isinstance(programs, types.GeneratorType):

        # LIST OF MULTILINE PROGRAMS

        if isinstance(programs, types.GeneratorType) or type(programs[0]) is list:
            return [render_program(program) for program in programs]

        # ONE MULTI-LINE PROGRAM

        elif type(programs[0]) is str:
            return [render_program(programs), ]
        else:
            raise Exception("Unknown program type")
    else:
        raise Exception("Unknown program type")


def render_program(program):
    return ''.join(['\t' + codeline + '\n' for codeline in program])
