import unittest

import requests

import python_template.config as cf


class TestOperationSync(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_health(self):
        url = f"http://{cf.HOST}:{cf.PORT}/health"

        response = requests.request("GET", url, headers={}, data={})
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json["status"], "OK")
