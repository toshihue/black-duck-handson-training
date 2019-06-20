import requests
import json
import sys
import datetime
requests.urllib3.disable_warnings()

# Authentication
def authenticate(base_url, api_key, verify = True):

    auth_url_path = '/api/tokens/authenticate'
    auth_response_data_format = 'application/vnd.blackducksoftware.user-4+json'

    auth_headers = {
        'Authorization': 'token ' + api_key,
        'Accept': auth_response_data_format
    }

    auth_response = requests.post(
        base_url + auth_url_path, headers = auth_headers, verify = verify)
    print(datetime.datetime.now(), sys._getframe().f_code.co_name+':', auth_response)
    
    if auth_response.ok:
        auth_response_json = auth_response.json()
        bearer_token = auth_response_json['bearerToken']
        # print(bearer_token)
        return bearer_token
    else:
        print('Error Message:', auth_response.text)
        sys.exit(1)



