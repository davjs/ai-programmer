__author__ = 'David'


def get_linear_equation(requirements: list, int_var: str):
    if len(requirements) > 1:
        prev_angle = None
        index_phases = []
        angles = {}
        return_statements = {}
        for index in range(len(requirements) - 1):
            curr_req = requirements[index]
            next_req = requirements[index + 1]
            x1 = curr_req.parameters[0]
            x2 = next_req.parameters[0]
            y1 = curr_req.output
            y2 = next_req.output
            angle = slope(x2 - x1, y2 - y1)
            if angle != prev_angle:
                angles[index] = angle
                prev_angle = angle
                index_phases.append(index)

        for index in index_phases:
            offset = get_offset(requirements[index].output, requirements[index].parameters[0], angles[index])
            str_offset = ""
            if offset != 0:
                str_offset = " + " + str(offset)
            return_statements[index] = ("return " + int_var + " * " + str(angles[index]) + str_offset)

        if len(index_phases) == 1:
            return return_statements[index_phases[0]]
        else:
            sourcecode = []
            for index in reversed(index_phases[1:]):
                condition = "if " + int_var + " > " + str(requirements[index].parameters[0]) + ':'
                sourcecode.append(condition)
                sourcecode.append("\t" + return_statements[index])
            sourcecode.append("else:")
            sourcecode.append("\t" + return_statements[index_phases[0]])
            return sourcecode


def slope(dx, dy):
    return int(dy / dx) if dx else None


def get_offset(y, x, k):
    return y - x * k
