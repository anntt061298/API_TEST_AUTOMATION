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

BASE_URL = f"https://dev1-retail-api.equix.app/v1/"

headers = {
    "Content-Type": "application/json",
    "environment": "tradeforgood",
}

USERNAME = "advisor01@gmail.com"
PASSWORD = "Ab@12345"

Payload = {
    "data": {
        "username": USERNAME,
        "password": PASSWORD,
        "provider": "paritech",
        "storage_token": True
    }
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
        pass

    def test01(self):
        """ Login.01: Login successfull """
        url = BASE_URL + "auth"
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)
        # print (response_data)

    def test02(self):
        """ Login.02: Login fail : Missing field Username """
        url = BASE_URL + "auth"

        Payload["data"]["username"] = ""
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)

    def test03(self):
        """ Login.03: Login fail : Delete  field Username """
        url = BASE_URL + "auth"

        del Payload["data"]["username"]
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)

    def test04(self):
        """ Login.04: Login fail : Enter wrong field Username """
        url = BASE_URL + "auth"

        Payload["data"]["username"] = "Ab@12233"
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)

    def test05(self):
        """ Login.05: Login fail : Missing field Password """
        url = BASE_URL + "auth"

        Payload["data"]["password"] = ""
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)

    def test06(self):
        """ Login.06: Login fail : Delete  field Password """
        url = BASE_URL + "auth"

        del Payload["data"]["password"] 
    
        # Send POST request
        status_code, response_data = send_request(
            url=url, method="POST", headers=headers, data = Payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 400)

    def test07(self):
        """ Login.07: Login fail : Enter wrong field Password """
        url = BASE_URL + "auth"
        MAX_LOGIN = 5
        Payload["data"]["password"] = "Ab@123"


                # Attempt to login 5 times with an invalid password
        for _ in range(MAX_LOGIN):
            status_code, response_data = send_request(
                url=url,
                method="POST",
                headers=headers,  # Replace with your actual headers
                data=Payload
            )

            # If the login attempt was successful, the test fails
            self.assertEqual(status_code, 400, f"Login attempt {_+1} succeeded unexpectedly")

        # After 5 failed attempts, the account should be locked
        status_code, response_data = send_request(
            url=url,
            method="POST",
            headers=headers,
            data=Payload
        )

        # Check for a specific error code or message indicating account lockout
        self.assertEqual(status_code, 400, "Account not locked after 5 failed attempts")
        # Add more specific assertions based on the expected response for account lockout
    

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