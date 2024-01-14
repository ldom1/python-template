import unittest

import python_template.config as cf
from python_template.example.example import Example


class TestExample(unittest.TestCase):
    def test_hello(self):
        example = Example()
        assert example.hello() == f"Hello, {cf.PROJECT_NAME}!"
