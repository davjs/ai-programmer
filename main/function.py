__author__ = 'david'


class Function:
    name = ""
    parameters = []
    func_def_text = ""
    requirements = []
    body_text = ""
    result = 0
    resulting_type = type(None)

    def addRequirement(self, *requirement):
        self.requirements.append(requirement)

    def execute(self, *arg):
        self.result = 0
        wrapper = \
            self.func_def_text + \
            "\t" + self.body_text + '\n' + \
            "self.result = " + self.name + "(" + ''.join(arg) + ")"
        exec(wrapper, locals())
        return self.result

    def __init__(self, name, parameters, resulting_type):  # string, list[Parameter], Type
        self.resulting_type = resulting_type
        self.data = []
        self.name = name
        self.parameters = parameters
        self.requirements = []
        # TODO: Write test for function prototype rendering
        parameter_string = ''.join([param.variable_name for param in parameters])
        self.func_def_text = "def " + name + "(" + parameter_string + "):\n"
