import python_template.config as cf


class Example:
    def __init__(self):
        self.name = cf.PROJECT_NAME

    def hello(self):
        return f"Hello, {self.name}!"
