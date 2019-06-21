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

# Get All Components
get_component_request_data_format = 'application/vnd.blackducksoftware.bill-of-materials-6+json'
get_component_response_data_format = 'application/vnd.blackducksoftware.bill-of-materials-6+json'
get_component_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': get_component_response_data_format,
    'Content-Type': get_component_request_data_format
}


####### Change here ##########
project_id = 'b1bf3f19-9660-442e-9477-c32e04398fcd'
project_version_id = 'd549cc89-9a54-4f59-943d-623a3bfbf8c5'
##############################

get_component_url_path = '/api/projects/' + project_id + \
    '/versions/' + project_version_id + '/components'

get_component_response = requests.get(
    base_url + get_component_url_path, headers=get_component_request_headers, verify=verify)

print(datetime.datetime.now(), os.path.basename(
    __file__) + ':', get_component_response)
if get_component_response.ok:

    get_component_response_json = get_component_response.json()
    formatted_json = json.dumps(get_component_response_json, indent=2)
    # print(formatted_json)
    os.makedirs('./output/', exist_ok=True)
    with open("./output/components.json", mode='w') as f:
        f.write(formatted_json)

    high_risk_count = 0
    medium_risk_count = 0
    low_risk_count = 0
    for item in get_component_response_json['items']:
        for count in item['securityRiskProfile']['counts']:
            if count['countType'] == 'LOW':
                low_risk_count += count['count']
            elif count['countType'] == 'MEDIUM':
                medium_risk_count += count['count']
            elif count['countType'] == 'HIGH':
                high_risk_count += count['count']

    print('High Vulnerabilities:', high_risk_count)
    print('Medium Vulnerabilities:', medium_risk_count)
    print('Low Vulnerabilities:', low_risk_count)
    print('Total Vulnerabilities:', high_risk_count +
          medium_risk_count + low_risk_count)
else:
    print('Error Message:', get_component_response.text)
    sys.exit(1)
