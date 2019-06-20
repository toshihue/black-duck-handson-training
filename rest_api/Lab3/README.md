# ユーザの読み取り
## 概要
[Lab2](../Lab2)で作成したユーザの情報を読み取ります。


## 課題
[Lab2](../Lab2)で作成したユーザの情報を表示させてください。
該当のUser IDはUI画面で確認してください。

### テンプレート

```read_user.py
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

# Reading a Single User
user_id = # Code here

user_response_data_format = 'application/vnd.blackducksoftware.user-4+json'
user_request_headers = {
    'Authorization': 'Bearer ' + bearer_token,
    # Code here
}

url_path = # Code here
user_response = # Code here

print(datetime.datetime.now(), os.path.basename(__file__) + ':', user_response)
user_response_json = user_response.json()
formatted_json = json.dumps(user_response_json, indent=2)
print(formatted_json)

if user_response.ok:
    with open("./output/read_user.json", mode='w') as f:
        f.write(formatted_json)


```

* 標準出力でjsonを見やすくするために、formatted_json = json.dumps(user_response_json, indent=2) で整形します。
* ユーザ情報のjsonをVS Codeなどで表示するため、リクエスト成功時にファイルに保存します。

### 解答例
[解答例](../read_user.py)
