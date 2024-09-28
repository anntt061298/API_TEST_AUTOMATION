#!/usr/bin/env python3

import os
import subprocess
import json
import requests
import configparser
import requests

def run_command(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res

def testcase_sort_func(a,b):
    names = [a,b]
    names.sort(reverse=True)
    return [1,-1][names[0] == b]



def login_success():
    
    url = "https://wts.finavi.com.vn/api/v1/login"

    # Headers
    headers = {
        "Content-Type": "application/json; charset=UTF-8",        
    }

    data = {
    "grant_type": "password",
    "client_id": "grooo",
    "client_secret": "grooo",
    "platform": "WEB",
    "username": "An061298",
    "password": "ThuAn061298"
}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        refresh_token = data.get("accessToken")
        return refresh_token
    else:
        print(f"Error refreshing access token: {response.status_code}")
        print(response.text)
        return None


def send_request(url, method, headers=None, data=None):
    status_code = None
    response_data = None

    if method == "GET":
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if response.status_code == 200:
            response_data =  response.json()
    elif method == "POST":
        response = requests.post(url, json=data, headers=headers)
        status_code = response.status_code
        if response.status_code == 200:
            response_data =  response.json()

    elif method == "PUT":
        response = requests.put(url, json=data, headers=headers)
        status_code = response.status_code
        if response.status_code == 200:
            response_data =  response.json()

    elif method == "DELETE":
        response = requests.delete(url, json=data, headers=headers)
        status_code = response.status_code
        if response.status_code == 200:
            response_data =  response.json()
            
    return [status_code, response_data]
