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

# Get a Single User by "userName" and "email"

user_url_path = '/api/users/'

user_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
user_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': user_response_data_format
}

### Change here ####
user_name = 'api_created_user1561067930'
first_name = 'api_created_user'
last_name = 'api_created_user'
email = 'api_created_user@example.com'
####################

user_params = {'q': 'userName:' + user_name + ',' + 'firstName:' +
               first_name + ',' + 'lastName:' + last_name + ',' + 'email' + email}


user_response = requests.get(
    base_url + user_url_path, headers=user_request_headers, params=user_params,  verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', user_response)
user_response_json = user_response.json()
# formatted_json = json.dumps(user_response_json, indent=2)
# print(formatted_json)
if user_response.ok:
    user_data = user_response.json()
    if user_data['totalCount'] == 1:
        # print('User:', user_data['items'][0]['_meta']['href'])
        user_url = str(user_data['items'][0]['_meta']['href'])
        user_id = user_url.split('/')[-1]
        print('User ID:', user_id)
    else:
        print('Error Message:', str(
            user_data['totalCount']) + ' user(s) matched')
else:
    print('Error Message:', user_response.text)


# Get a Single Group by "GroupName"
group_url_path = '/api/usergroups/'

group_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
group_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': group_response_data_format
}

### Change here ####
group_name = 'api_created_group1561068667'
####################

group_params = {'q': group_name}

group_response = requests.get(
    base_url + group_url_path, headers=group_request_headers, params=group_params,  verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', group_response)
group_response_json = group_response.json()
# formatted_json = json.dumps(group_response_json, indent=2)
# print(formatted_json)
if group_response.ok:
    group_data = group_response.json()
    if group_data['totalCount'] == 1:
        group_url = str(group_data['items'][0]['_meta']['href'])
        print('Group URL:', group_url)
    else:
        print('Error Message:', str(
            group_data['totalCount']) + ' group(s) matched')
else:
    print('Error Message:', group_response.text)


# Assign a User to a Group

assignment_url_path = '/api/users/' + user_id + '/usergroups'

assignment_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
assignment_request_data = [
    {
        "userGroupUrl": group_url
    }
]

assignment_request_json = json.dumps(
    assignment_request_data).encode('utf-8')

assignment_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
assignment_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
assignment_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Content-Type': assignment_request_data_format
}

assignment_response = requests.post(
    base_url + assignment_url_path, headers=assignment_request_headers, data=assignment_request_json,  verify=verify)

print(datetime.datetime.now(), os.path.basename(
    __file__) + ':', assignment_response)

if assignment_response.ok:
    print('The user has been assigned to the group successfully')
else:
    print('Error Message:', assignment_response.text)
    