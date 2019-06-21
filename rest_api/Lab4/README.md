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
verify = ini_file.getboolean('credential', 'verify')

# Authentication
api_key = ini_file.get('credential', 'api_key')
bearer_token = rest_api_auth.authenticate(
    base_url=base_url, api_key=api_key, verify=verify)

# Code here
```

* group_nameにstr(int(datetime.datetime.now().timestamp()))などを結合させると、実行毎にユニークになるため試行に便利です。

### 解答例
[解答例](../create_group.py)