import requests
import json
import configparser
requests.urllib3.disable_warnings()

ini_file = configparser.ConfigParser()
ini_file.read('./config.ini', 'UTF-8')

base_url = ini_file.get('credential', 'base_url')
verify = ini_file.getboolean('credential', 'verify')

# Authentication
api_key = ini_file.get('credential', 'api_key')

auth_headers = {
    'Authorization': 'token ' + api_key,
    'Accept': 'application/vnd.blackducksoftware.user-4+json'
}
url = base_url + '/api/tokens/authenticate'
response = requests.post(url, headers=auth_headers, verify=verify)
print(response)
print(response.text)