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

Account = "050C158527"


class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Access_Token = login_success()
        time.sleep(1)

    def setUp(self):

        self.base_url = BASE_URL+ "bridge/Account/GetMyStockList"

        self.params = {
            "CUSTODYCD": Account
        }

        self.header = {
        "Content-Type": "application/json; charset=UTF-8"  ,     
        "Authorization":  f"Bearer {CurlTest.Access_Token}"
    }
 

    # @unittest.skip("skipped")
    def test_001(self): 
        """ GET_MY_STOCK_LIST_001: Get My stock list success """

        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="GET", headers=self.header, params= self.params
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)     

    # @unittest.skip("skipped")
    def test_002(self):
        """ GET_MY_STOCK_LIST_002: Get My stocklist when miss param  """

        url = BASE_URL + "user/info"

        # Send POST request
        status_code, response_data = send_request(
            self.base_url,  method="GET", headers= self.header
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

    # @unittest.skip("skipped")
    def test_003(self):
        """ GET_MY_STOCK_LIST_003: Get My stocklist when enter param null  """

        url = BASE_URL + "user/info"

        self.params["CUSTODYCD"]= ""
        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="GET",  headers= self.header, params= self.params
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

    # @unittest.skip("skipped")
    def test_004(self):
        """ GET_MY_STOCK_LIST_004: Get My stocklist when enter param invalid  """

        url = BASE_URL + "user/info"

        self.params["CUSTODYCD"]= "123"

        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="GET",  headers= self.header, params= self.params
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

    # @unittest.skip("skipped")
    def test_005(self):
        """ GET_MY_STOCK_LIST_005: Get My stocklist when missing token """

        url = BASE_URL + "user/info"

        del self.header["Authorization"]

        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="GET", headers= self.header, params= self.params
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 401)

        # @unittest.skip("skipped")
    def test_006(self):
        """ GET_MY_STOCK_LIST_006: Get My stocklist when enter token invalid """

        url = BASE_URL + "user/info"
        self.header["Authorization"] = "123"
        # Send POST request
        status_code, response_data = send_request(
            self.base_url, method="GET", headers= self.header, params= self.params
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