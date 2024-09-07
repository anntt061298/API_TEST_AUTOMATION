#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import unittest
# fast_api_root.py
import sys
import os

# Thêm thư mục cha của test_utils vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Bây giờ bạn có thể nhập test_utils
from test_utils import *

BASE_URL = f"https://todo.pixegami.io/"


# comment

class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    
    def test01(self):
        """GET.01: Get Root successfully"""

        url = "https://todo.pixegami.io/"

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET"
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)
        self.assertEqual(response_data["message"],"Hello World from Todo API")
        print(response_data)
if __name__ == "__main__":
    from argparse import ArgumentParser

    print("Running Test Suite")

    script = ArgumentParser(description=TEST_SUITE_NAME, epilog="Note: any note here")
    # script.add_argument("Config", type=str, help="Config file")
    args, unittest_args = script.parse_known_args()

    from test_utils import testcase_sort_func

    unittest.defaultTestLoader.sortTestMethodsUsing = testcase_sort_func

    from framework import CustomTestRunner

    unittest.main(argv=[__file__] + unittest_args, testRunner=CustomTestRunner)