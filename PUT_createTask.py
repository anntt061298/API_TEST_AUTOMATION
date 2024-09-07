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

BASE_URL = f"https://todo.pixegami.io"
CONTENT = "contentnew"
USERID = "12"
TASKID = "12"

payload = {
  "content": CONTENT,
  "user_id": USERID,
  "task_id": TASKID,
  "is_done": False
}

class CurlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    
    def test01(self):
        """PUT.01: PUT create task successfully """

        url = f"{BASE_URL}/create-task"

        # Send POST request
        status_code, response_data = send_request(
            url=url, method="PUT", data=payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 200)
        # print(response_data)
        self.assertEqual(response_data["task"]["user_id"], USERID)
        self.assertEqual(response_data["task"]["content"], CONTENT)

    
    def test02(self):
        """PUT.02: Delete field content """

        url = "https://todo.pixegami.io/create-task"
        
        del payload["content"]


        # Send POST request
        status_code, response_data = send_request(
            url=url, method="PUT", data=payload
        )

        # Validate HTTP response code, fail if not 200
        self.assertEqual(status_code, 422)
        print(status_code)

    

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