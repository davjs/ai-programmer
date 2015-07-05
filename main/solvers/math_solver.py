__author__ = 'David'


def get_linear_equation(int_var: str, requirements: list, interpolate=True):
    if len(requirements) > 1:
        prev_angle = None
        prev_offset = None
        index_phases = []
        angles = {}
        offsets = {}
        return_statements = {}
        error = 1
        for index in range(len(requirements) - 1):
            curr_req = requirements[index]
            next_req = requirements[index + 1]
            x1 = curr_req.parameters[0]
            x2 = next_req.parameters[0]
            y1 = curr_req.output
            y2 = next_req.output
            #TODO: make line class?
            angle = slope(x2 - x1, y2 - y1)
            offset = get_offset(y1, x1, angle)
            if angle != prev_angle or offset != prev_offset:
                if interpolate or error > 0:
                    angles[index] = angle
                    offsets[index] = offset
                    #  TODO: use index - 1 in array ?
                    prev_angle = angle
                    prev_offset = offset
                    index_phases.append(index)
                    error = 0
                else:
                    error += 1

        for index in index_phases:
            offset = offsets[index]
            str_offset = ""
            str_multiply = ""
            if angles[index] != 0:
                str_multiply = int_var + " * " + str(angles[index])
            if offset != 0:
                str_offset = str(offset)
            if len(str_offset) > 0 and len(str_multiply) > 0:
                str_offset = " + " + str_offset
            if len(str_offset) == len(str_multiply) == 0:
                str_offset = "0"
            return_statements[index] = ("return " + str_multiply + str_offset)

        if len(index_phases) == 1:
            return [return_statements[index_phases[0]]]
        else:
            sourcecode = []
            for index in reversed(index_phases[1:]):
                condition = "if " + int_var + " >= " + str(requirements[index].parameters[0]) + ':'
                sourcecode.append(condition)
                sourcecode.append("\t" + return_statements[index])
            sourcecode.append("else:")
            sourcecode.append("\t" + return_statements[index_phases[0]])
            return sourcecode


def slope(dx, dy):
    return int(dy / dx) if dx else None


def get_offset(y, x, k):
    return y - x * k
