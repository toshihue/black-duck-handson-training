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

# Creating a Group
group_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
group_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
group_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': group_response_data_format,
    'Content-Type': group_request_data_format
}

group_url_path = '/api/usergroups'
### Change here ####
group_name = 'api_created_group' + \
    str(int(datetime.datetime.now().timestamp()))
active = True
####################
group_request_data = {
    'active': active,
    'name': group_name
}

group_request_json = json.dumps(group_request_data).encode('utf-8')
group_response = requests.post(
    base_url + group_url_path, headers=group_request_headers, data=group_request_json, verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', group_response)
if group_response.ok:
    group_response_json = group_response.json()
    group_url = str(group_response_json['_meta']['href'])
    group_id = group_url.split('/')[-1]
    print('Group Name:', group_name)
    print('Group ID:', group_id)
else:
    print('Error Message:', group_response.text)
    sys.exit(1)

# Assign a Global Role to a Group
global_assignment_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
global_assignment_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
global_assignment_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': global_assignment_response_data_format,
    'Content-Type': global_assignment_request_data_format
}

global_assignment_url_path = '/api/usergroups/' + group_id + '/roles'

### Change here ####
global_assignment_role_id = '00000001-0001-0001-0001-000000000009'  # Global Code Scanner
####################

global_assignment_request_data = {
    'role': base_url + '/api/roles/' + global_assignment_role_id
}

global_assignment_request_json = json.dumps(
    global_assignment_request_data).encode('utf-8')
global_assignment_response = requests.post(
    base_url + global_assignment_url_path, headers=global_assignment_request_headers, data=global_assignment_request_json, verify=verify)
print(datetime.datetime.now(), os.path.basename(
    __file__) + ':', global_assignment_response)

if global_assignment_response.ok:
    global_assignment_response_json = global_assignment_response.json()
    formatted_json = json.dumps(global_assignment_response_json, indent=2)
    # print(formatted_json)    
    with open("./output/global_assignment.json", mode='w') as f:
        f.write(formatted_json)
else:
    print('Error Message:', global_assignment_response.text)
    sys.exit(1)


# Assign Existing Project with a Role to a Group
project_assignment_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
project_assignment_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
project_assignment_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': project_assignment_response_data_format,
    'Content-Type': project_assignment_request_data_format
}

project_assignment_url_path = '/api/usergroups/' + group_id + '/roles'

### Change here ####
project_assignment_role_id = '00000001-0001-0001-0001-00000000000b'  # BOM Manager
project_assignment_project_id = 'b1bf3f19-9660-442e-9477-c32e04398fcd'
####################

project_assignment_request_data = {
    'role': base_url + '/api/roles/' + project_assignment_role_id,
    'scope': base_url + '/api/projects/' + project_assignment_project_id
}

project_assignment_request_json = json.dumps(
    project_assignment_request_data).encode('utf-8')
project_assignment_response = requests.post(
    base_url + project_assignment_url_path, headers=project_assignment_request_headers, data=project_assignment_request_json, verify=verify)
print(datetime.datetime.now(), os.path.basename(
    __file__) + ':', project_assignment_response)

if project_assignment_response.ok:
    project_assignment_response_json = project_assignment_response.json()
    formatted_json = json.dumps(project_assignment_response_json, indent=2)
    # print(formatted_json)    
    with open("./output/project_assignment.json", mode='w') as f:
        f.write(formatted_json)    
else:
    print('Error Message:', project_assignment_response.text)
    sys.exit(1)
