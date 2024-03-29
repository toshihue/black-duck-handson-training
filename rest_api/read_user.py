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

# Reading a Single User

### Change here ####
user_id = 'a99360a7-c2bc-4244-95e5-ed0c4f706549' 
####################

user_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
user_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': user_response_data_format
}

url_path = '/api/users/'+user_id
user_response = requests.get(
    base_url + url_path, headers=user_request_headers, verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', user_response)
user_response_json = user_response.json()
formatted_json = json.dumps(user_response_json, indent=2)
# print(formatted_json)

if user_response.ok:
    os.makedirs('./output/', exist_ok=True)
    with open("./output/read_user.json", mode='w') as f:
        f.write(formatted_json)

