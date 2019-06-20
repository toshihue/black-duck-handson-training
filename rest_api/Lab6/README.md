# グループへのユーザ割当
## 概要
最後にロールの割り当てが完了したグループに、所属するユーザを割り当てます。


## 課題
既存のユーザを既存グループに割り当てます。（ユーザ、グループ作成用csvのみを持っていて、ユーザ名とグループ名のみを知っている前提とします。）
1. ユーザのURLは情報としてもっていないため、ユーザ名等からユーザのIDを引き当てます。
2. グループのURLは情報としてもっていないため、グループ名からグループのURLを引き当てます。
3. 取得したユーザのIDとグループのURLでグループへのユーザ割当を行います。
    * Swagger(REST API Developers Guide)から必要なエンドポイントを探します。 


### テンプレート

```assign_user_to_group.py
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

# Get a Single User by "userName" and "email"

user_url_path = '/api/users/'

user_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
user_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'Accept': user_response_data_format
}

### Change here ####
user_name = # Code here
first_name = # Code here
last_name = # Code here
email = # Code here
####################

user_params = {'q': # Code here}


user_response = requests.get(
    base_url + user_url_path, headers=user_request_headers, params=user_params,  verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', user_response)
user_response_json = user_response.json()
# formatted_json = json.dumps(user_response_json, indent=2)
# print(formatted_json)
if user_response.ok:
    user_data = user_response.json()
    if user_data['totalCount'] == # Code here:
        # print('User:', user_data['items'][0]['_meta']['href'])
        user_url = # Code here
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
group_name = # Code here
####################

group_params = {# Code here}

group_response = requests.get(
    base_url + group_url_path, headers=group_request_headers, params=group_params,  verify=verify)

print(datetime.datetime.now(), os.path.basename(__file__) + ':', group_response)
group_response_json = group_response.json()
# formatted_json = json.dumps(group_response_json, indent=2)
# print(formatted_json)
if group_response.ok:
    group_data = group_response.json()
    if group_data['totalCount'] == # Code here:
        group_url = # Code here
        print('Group URL:', group_url)
    else:
        print('Error Message:', str(
            group_data['totalCount']) + ' group(s) matched')
else:
    print('Error Message:', group_response.text)


# Assign a User to a Group

assignment_url_path = # Code here

assignment_request_data_format = 'application/vnd.blackducksoftware.user-4+json'
assignment_request_data = [
    {
        "userGroupUrl": # Code here
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

```


* 現状は、ユーザ、グループとも名前によるFilter機能はありません。
* 名前からIDやURLを引き当てるには、部分一致となるSearch機能で絞り込む必要があります。部分一致であるため、複数件になる可能性があり、必ず件数が1件であるチェックを行ってください。
* もしくはユーザやグループ自動作成時にURLをCSV等に保存するような仕組みにしてください。


### 解答例
[解答例](../assign_user_to_group.py)
