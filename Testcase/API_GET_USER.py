#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import unittest
# fast_api_root.py
import sys
import os
import time
import copy



# Thêm thư mục cha của test_utils vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Bây giờ bạn có thể nhập test_utils
from test_utils import *

BASE_URL = f"https://wts.finavi.com.vn/api/v1/"
headers = {
        "Content-Type": "application/json; charset=UTF-8"        
    }



class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Access_Token = login_success()
        time.sleep(1)

    def setUp(self):
    # This method will be run before each test case
        pass

    # @unittest.skip("skipped")
    def test01(self):
        """ Login.01:Get success userinfo  """

        url = BASE_URL + "user/info"

        headers = {
            "Authorization": f"Bearer {CurlTest.Access_Token}",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)
        

    # @unittest.skip("skipped")
    def test02(self):
        """ Login.02: Wrong with missing enter token  """

        url = BASE_URL + "user/info"

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 401)

    # @unittest.skip("skipped")
    def test03(self):
        """ Login.03: Wrong with token invalid """

        url = BASE_URL + "user/info"

        headers = {
            "Authorization": "123",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 401)

    # @unittest.skip("skipped")
    def test04(self):
        """ Login.03: Wrong with token expire """

        url = BASE_URL + "user/info"

        headers = {
            "Authorization": "",
        }

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="GET", headers=headers
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 401)
 
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