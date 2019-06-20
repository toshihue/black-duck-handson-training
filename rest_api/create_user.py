import requests
import json
import rest_api_auth
import sys
import datetime
import os
import configparser
# logging.basicConfig(level=logging.DEBUG)
requests.urllib3.disable_warnings()

ini_file = configparser.ConfigParser()
ini_file.read('./config.ini', 'UTF-8')

base_url = ini_file.get('credential', 'base_url')
verify = ini_file.getboolean('credential', 'verify')

# Authentication
api_key = ini_file.get('credential', 'api_key')
bearer_token = rest_api_auth.authenticate(
    base_url=base_url, api_key=api_key, verify=verify)

# Creating a User
user_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
user_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
user_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': user_response_data_format,
    'Content-Type': user_request_data_format
}

### Change here ####
url_path = '/api/users'
user_name = 'api_created_user' + str(int(datetime.datetime.now().timestamp()))
first_name = 'api_created_user'
last_name = 'api_created_user'
email = 'api_created_user@example.com'
active = True
password = '2,Dkc+:g&:'
####################

user_request_data = {
    'userName': user_name,
    'firstName': first_name,
    'lastName': last_name,
    'email': email,
    'active': active,
    'password': password
}

user_request_json = json.dumps(user_request_data).encode('utf-8')
user_response = requests.post(
    base_url + url_path, headers=user_request_headers, data=user_request_json, verify=verify)
print(datetime.datetime.now(), os.path.basename(__file__) + ':', user_response)
if user_response.ok:
    user_response_json = user_response.json()
    # formatted_json = json.dumps(user_response_json, indent=2)
    # print(formatted_json)
    print('Created User Name:', user_name)

else:
    print('Error Message:', user_response.text)


