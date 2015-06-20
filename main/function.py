__author__ = 'david'


class Requirement:
    parameters = ()
    output = None

    def __init__(self, parameters, output):
        self.parameters = parameters
        self.output = output


class Function:
    name = ""
    parameters = []
    func_def_text = ""
    requirements = []
    body_text = ""
    result = 0
    resulting_type = type(None)

    def add_requirement(self, requirement: Requirement):
        self.requirements.append(requirement)

    def execute(self, parameters: []):
        parameters = [str(param) for param in parameters]
        parameters = "(" + ','.join(parameters) + ")"
        print(parameters)
        self.result = 0
        wrapper = \
            self.func_def_text + \
            self.body_text + \
            "self.result = " + self.name + parameters
        exec(wrapper, locals())
        return self.result

    def __init__(self, name, parameters, resulting_type):  # string, list[Parameter], Type
        self.resulting_type = resulting_type
        self.data = []
        self.name = name
        self.parameters = parameters
        self.requirements = []
        # TODO: Write test for function prototype rendering
        parameter_string = ','.join([param.variable_name for param in parameters])
        self.func_def_text = "def " + name + "(" + parameter_string + "):\n"
