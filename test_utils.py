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

# def read_refresh_token_config(config_file='config1.ini'):
#     config = configparser.ConfigParser()
#     config.read(config_file)
#     return config

def login_success():
    
    url = "https://dev2-retail-api.equix.app/v1/auth"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "environment": "equix",
    }

    data = {
    "data": {
        "username": "thu-an.nguyen@novus-fintech.com",
        "password": "Ab@12345",
        "provider": "paritech",
        "storage_token": True
    }
}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        refresh_token = data.get("refreshToken")
        return refresh_token
    else:
        print(f"Error refreshing access token: {response.status_code}")
        print(response.text)
        return None
    
def decode(refresh_token):
    url = "https://dev2-retail-api.equix.app/v1/auth/decode"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "environment": "equix",
    }

    data = {
    "data": {
        "token": refresh_token,
        "pin": "111111"
    }
}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        return token
    else:
        print(f"Error refreshing access token: {response.status_code}")
        print(response.text)
        return None    

def read_refresh_token_config(file_name='config1.ini'):
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = current_path+ "/" + file_name

    config = configparser.ConfigParser()
    config.read(file_path)

    section = 'DEFAULT'
    key = 'refresh-token'

    refresh_token = config.get(section, key)
    return refresh_token

def refresh_access_token(token):
    url = "https://dev2-retail-api.equix.app/v1/auth/refresh"

    # Headers
    headers = {
        "Content-Type": "application/json",
        "environment": "tradeforgood",
        "origin": "https://dev2.equix.app"

    }

    data = {
        "data": {
            "refreshToken": token,
            "deviceID": "4216cf3e-108a-4738-958b-3420f3523557",
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        data = response.json()
        new_access_token = data.get("accessToken")
        return new_access_token
    else:
        print(f"Error refreshing access token: {response.status_code}")
        print(response.text)
        return None
    

# try:
#     refresh_token = login_success()
#     if refresh_token:
#         print('Refresh Token:', refresh_token)
        
#         token = decode(refresh_token)
#         if token:
#             print('Token:', token)
#             new_access_token = refresh_access_token(token)
#             if new_access_token:
#                 print('new_access_token:', new_access_token)
#             else:
#                 print('Failed to get new access token.')
#         else:
#             print('Failed to get token.')
#     else:
#         print('Failed to get refresh token.')
# except Exception as e:
#     print(str(e))


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
