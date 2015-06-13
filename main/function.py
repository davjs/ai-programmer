__author__ = 'david'

class Function:
    name = ""
    parameters = ()
    func_def_text = ""
    requirements = []
    body_text = ""
    result = 0

    def addRequirement(self,*requirement):
        self.requirements.append(requirement)

    def execute(self,*arg):
        self.result = 0
        wrapper = \
            self.func_def_text + \
            "\t" + self.body_text + '\n' + \
            "self.result = " + self.name + "(" + ''.join(arg) + ")"
        exec(wrapper,locals())
        return self.result

    def __init__(self,name,*parameters):
        self.data = []
        self.name = name
        self.parameters = parameters
        self.requirements = []
        self.func_def_text = "def " + name + "(" + ''.join(parameters) + "):\n"
