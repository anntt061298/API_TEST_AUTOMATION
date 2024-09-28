#!/usr/bin/env python3

TEST_SUITE_NAME = "Sample Test API"

import unittest
# fast_api_root.py
import sys
import os
import time
from datetime import datetime


# Thêm thư mục cha của test_utils vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Bây giờ bạn có thể nhập test_utils
from test_utils import *

BASE_URL = f"https://wts.finavi.com.vn/api/v1/"
name_exist = "ddd"

class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Access_Token = login_success()
        time.sleep(1)

    def setUp(self):

        timestamp = str(datetime.now().timestamp())

        self.base_url = BASE_URL+ "favorite"

        self.Payload = {
            "name": "fav" + timestamp
        }

        self.header = {
        "Content-Type": "application/json; charset=UTF-8"  ,     
        "Authorization":  f"Bearer {CurlTest.Access_Token}"
    }
 

    # @unittest.skip("skipped")
    def test_001(self): 
        """CREATE_FAVORITE_001: Create my favorite success """

        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)     

    # @unittest.skip("skipped")
    def test_002(self):
        """CREATE_FAVORITE_002: Create favorite fail when mising name """

        self.Payload["name"]= ""
        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

    # @unittest.skip("skipped")
    def test_003(self):
        """CREATE_FAVORITE_003: Create favorite fail when deleate name """

        del self.Payload["name"]
        
        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

    # @unittest.skip("skipped")
    def test_004(self):
        """CREATE_FAVORITE_004: Create favorite fail when enter Name existed """

        self.Payload["name"]= name_exist

        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)

    # @unittest.skip("skipped")
    def test_005(self):
        """CREATE_FAVORITE_005: Create favorite fail when enter Name exceed maxlength 20 """

        name = "a"*21
        self.Payload["name"]= name

        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

        # @unittest.skip("skipped")
    def test_006(self):
        """CREATE_FAVORITE_006: Create favorite fail  when enter token invalid """

        self.header["Authorization"] = "123"
        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 401)

    def test_007(self):
        """CREATE_FAVORITE_007: Create favorite fail  when missing enter token """

        del self.header["Authorization"]
        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="POST", headers=self.header, data = self.Payload
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