# グループの作成
## 概要
グループの作成をします。


## 課題
グループを作成し、作成したGroupのURLを表示してください。

### テンプレート

```create_group.py
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
verify = bool(ini_file.get('credential', 'verify'))

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

url_path = # Code here
active = #Code here
group_name = # Code here + str(int(datetime.datetime.now().timestamp()))
    
group_request_data = {
    'active': active,
    'name': group_name
}

group_request_json = json.dumps(group_request_data).encode('utf-8')
group_response = requests.post(
    base_url + url_path, headers=group_request_headers, data=group_request_json, verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', group_response)
if group_response.ok:
    group_data = group_response.json()
    formatted_json = json.dumps(group_data, indent=2)
    #print(formatted_json)
    with open("./output/create_group.json", mode='w') as f:
        f.write(formatted_json)    
    print('Created Group URL:', # Code here)
else:
    print('Error Message:', group_response.text)

```

* group_nameにstr(int(datetime.datetime.now().timestamp()))などを結合させると、実行毎にユニークになるため試行に便利です。

### 解答例
[解答例](../create_group.py)