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

# Get All Snippet-matched Components
get_component_request_data_format = 'application/vnd.blackducksoftware.bill-of-materials-6+json'
get_component_response_data_format = 'application/vnd.blackducksoftware.bill-of-materials-6+json'
get_component_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': get_component_response_data_format,
    'Content-Type': get_component_request_data_format
}

get_component_filter_key = 'bomMatchType'
get_component_filter_value = 'snippet'
get_component_params = {
    'filter': get_component_filter_key + ':' + get_component_filter_value}

####### Change here ##########
project_id = 'b1bf3f19-9660-442e-9477-c32e04398fcd'
project_version_id = 'd549cc89-9a54-4f59-943d-623a3bfbf8c5'
##############################

get_component_url_path = '/api/projects/' + project_id + \
    '/versions/' + project_version_id + '/components'

get_component_response = requests.get(
    base_url + get_component_url_path, headers=get_component_request_headers, params=get_component_params, verify=verify)

print(datetime.datetime.now(), os.path.basename(
    __file__) + ':', get_component_response)
if get_component_response.ok:

    add_component_request_data_format = 'application/vnd.blackducksoftware.bill-of-materials-6+json'
    add_component_response_data_format = 'application/vnd.blackducksoftware.bill-of-materials-6+json'
    add_component_request_headers = {
        'Authorization': 'Bearer ' + bearer_token,
        'Accept': add_component_response_data_format,
        'Content-Type': add_component_request_data_format
    }
    add_component_url_path = '/api/projects/' + project_id + \
        '/versions/' + project_version_id + '/components'

    get_component_data = get_component_response.json()
    # get_component_count = str(get_component_data['totalCount'])
    for item in get_component_data['items']:
        add_component_version_url = item['componentVersion']
        add_component_data = {
            'component': add_component_version_url,
            'componentModification': str(datetime.datetime.now()) + ' Manually added for snippet-matched component by REST API',
            'componentModified': True
        }
        add_component_request_json = json.dumps(
            add_component_data).encode('utf-8')
        add_component_response = requests.post(
            base_url + add_component_url_path, headers=add_component_request_headers, data=add_component_request_json, verify=verify)
        print(datetime.datetime.now(), os.path.basename(
            __file__) + ':', get_component_response)
        if add_component_response.ok:
            print('Added Component:',
                  item['componentName'], item['componentVersionName'])
        else:
            print('Error Message:', add_component_response.text)

else:
    print('Error Message:', get_component_response.text)
    sys.exit(1)
