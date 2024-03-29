import python_template.config as cfg


class Example:
    """
    Example class for the Python template project.

    This class serves as a simple demonstration of how to utilize a global configuration
    within a Python class. It showcases the use of global configuration parameters,
    such as the project name, and how these can be employed within specific class methods.
    """

    name = cfg.PROJECT_NAME

    def hello(self):
        """
        Returns a greeting message.

        This method generates a greeting message that includes the project name, illustrating
        how class attributes can be utilized within its methods.

        Returns:
            str: A string containing the greeting message.
        """
        return f"Hello, {self.name}!"
