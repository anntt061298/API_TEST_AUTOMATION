#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import unittest
# fast_api_root.py
import sys
import os
import time


# Thêm thư mục cha của test_utils vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Bây giờ bạn có thể nhập test_utils
from test_utils import *

BASE_URL = f"https://dev2-operator-api.equix.app/v1/"

headers = {
    "Content-Type": "application/json",
    "environment": "equix",
}

ACCOUNT_ID = 108723

class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        refresh_token = login_success()
        time.sleep(1)

        token = decode(refresh_token)
        time.sleep(1)

        cls.access_token = refresh_access_token(token)
        # print(cls.access_token)

    def setUp(self):
    # This method will be run before each test case
        pass

    def test01(self):
        """ Login.01: Get portfolio successfull """
        url = BASE_URL + "portfolio/total/108723"

        headers = {
            "Authorization": f"Bearer {CurlTest.access_token}",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)

        
        # print (response_data)


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