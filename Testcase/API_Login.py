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
        "Content-Type": "application/json; charset=UTF-8",        
    }
USERNAME = "An061298"
PASSWORD = "ThuAn061298"

PAYLOAD = {
    "grant_type": "password",
    "client_id": "grooo",
    "client_secret": "grooo",
    "platform": "WEB",
    "username": USERNAME,
    "password": PASSWORD
}

class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        # refresh_token = read_refresh_token_config()
        # time.sleep(2)
        # cls.access_token = refresh_access_token(refresh_token)

    def setUp(self):
    # This method will be run before each test case
        # self.payload = dict(PAYLOAD)  # Khôi phục bản sao của PAYLOAD
        self.payload = copy.deepcopy(PAYLOAD)  # Tạo bản sao của PAYLOAD

    # @unittest.skip("skipped")
    def test01(self):
        """ Login.01: Login successfull """
        url = BASE_URL + "login"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)
        # print(response_data)
        self.assertEqual(response_data["accountList"][0]["id"], 10)
        self.assertEqual(response_data["accountList"][0]["userId"], 8)
        self.assertEqual(response_data["accountList"][0]["nickName"], "NM")
        self.assertEqual(response_data["accountList"][0]["accountNumber"], "050C158527")
        self.assertEqual(response_data["accountList"][0]["subNumber"], "0001158527NM")
        self.assertEqual(response_data["accountList"][0]["cusType"], "I")

    # @unittest.skip("skipped")
    def test02(self):
        """ Login.02: Login fail : Missing field grant_type """
        url = BASE_URL + "login"

        self.payload["grant_type"] = ""
        # print(PAYLOAD)
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test03(self):
        """ Login.03: Login fail : Delete field grant_type """
        url = BASE_URL + "login"

        del self.payload["grant_type"] 
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test04(self):
        """ Login.04: Login fail : Missing enter client_id  """
        url = BASE_URL + "login"

        self.payload["client_id"] = ""
        # print(self.payload)
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test05(self):
        """ Login.05: Login fail : Delete field client_id  """
        url = BASE_URL + "login"

        del self.payload["client_id"] 
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test06(self):
        """ Login.06: Login fail : Missing enter field client_secret  """
        url = BASE_URL + "login"

        self.payload["client_secret"] = ""
    
        # Send POST PAYLOAD
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test07(self):
        """ Login.07: Login fail : Delete field client_secret  """
        url = BASE_URL + "login"

        del self.payload["client_secret"]
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test08(self):
        """ Login.08: Login fail : Missing enter field platform  """
        url = BASE_URL + "login"

        self.payload["platform"] =""
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)

    # @unittest.skip("skipped")
    def test09(self):
        """ Login.09: Login fail : Delete field platform  """
        url = BASE_URL + "login"

        del self.payload["platform"]
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        # print (response_data)


    # @unittest.skip("skipped")
    def test10(self):
        """ Login.10: Login fail : Missing enter field Username """
        url = BASE_URL + "login"

        self.payload["username"] = ""
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)

    # @unittest.skip("skipped")
    def test11(self):
        """ Login.11: Login fail : Delete field Username """
        url = BASE_URL + "login"

        del self.payload["username"]
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)


    # @unittest.skip("skipped")
    def test12(self):
        """ Login.12: Login fail : Enter username dont exist """
        url = BASE_URL + "login"

        self.payload["username"] = "USLorem Ipsum is simply dummy text of the printing and typesetting industry.ERNAME"
        # print(self.payload)

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)
    

    # @unittest.skip("skipped")
    def test13(self):
        """ Login.13: Login fail : Enter password wrong """
        url = BASE_URL + "login"

        self.payload["password"] = "USLorem Ipsum is simply dummy text of the printing and typesetting industry.ERNAME"
        # print(self.payload)

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = self.payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)
        # print(response_data)
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