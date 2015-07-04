__author__ = 'david'



def find_pattern(breaking_points: list):
    if len (breaking_points) <= 1:
        return 0
    first_diff = breaking_points[1] - breaking_points[0]
    for i in range(1, len(breaking_points)):
        diff = breaking_points[i] - breaking_points[i-1]
        if diff != first_diff:
            return 0

    return first_diff


def bool_from_int(inputs: list, outputs: list):
    breaking_points = get_breaking_points(inputs, outputs)
    print(outputs)
    print(breaking_points)
    pattern = find_pattern(breaking_points)
    if pattern != 0:
        sourcecode = from_pattern(pattern)
    else:
        sourcecode = from_breaking_point(breaking_points, inputs)
    return sourcecode

def from_pattern(pattern):
    return "return x % " + str(pattern + 1) + " == 0"

def get_breaking_points(inputs: list, outputs: list):
    start_value = outputs[0]
    last_value = start_value
    breaking_points = []
    for i in range(len(inputs)):
        _input = inputs[i]
        output = outputs[i]
        if output != last_value:
            breaking_points.append(_input)
            last_value = output
    return breaking_points

def from_breaking_point(breaking_points: list, inputs: list):
    sourcecode = \
        ["if x >= " + str(breaking_point) + ":\n\treturn False" for breaking_point in breaking_points]
    sourcecode = '\n'.join(sourcecode)
    return sourcecode + "\nreturn True"

#print(bool_from_int([1, 2, 3, 4, 5, 6, 7, 8, 9], [True, True, True, True, False, False, False, False, False]))
#print("\n\n")
#print(bool_from_int([1, 2, 3, 4, 5, 6, 7, 8, 9], [True, False, True, False, True, False, True, False, True]))

ints = []
bools = []
for x in range(9):
    bools.append(x % 3 == 0)
    ints.append(x)

print(bools)
print(bool_from_int(ints, bools))
