import unittest

from python_template.example import Example


class TestExample(unittest.TestCase):
    def test_hello(self):
        example = Example()
        assert example.hello() == "Hello, python-project-template!"
