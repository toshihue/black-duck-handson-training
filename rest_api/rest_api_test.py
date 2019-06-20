import requests
import json
requests.urllib3.disable_warnings()

api_key = '' # add API key

auth_headers = {
    'Authorization': 'token ' + api_key,
    'Accept': 'application/vnd.blackducksoftware.user-4+json'
}
url = 'https://<hub_base_url>/api/tokens/authenticate'
response = requests.post(url, headers=auth_headers, verify=False)
print(response)
print(response.text)