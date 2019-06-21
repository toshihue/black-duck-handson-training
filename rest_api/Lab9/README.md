# ネットワーク経由で攻撃可能な脆弱性一覧表示
## 概要
ネットワーク経由で攻撃可能な脆弱性から対処できるよう、一覧表示をする。


## 課題
ネットワーク経由で攻撃可能な脆弱性をcvss3スコアで絞り込み、一覧表示をする。
コンポーネントからさらに脆弱性の情報を引き当てる必要がある。


### テンプレート

```get_network_reachable_vulnerabilities_in_bom
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


```



### 解答例
[解答例](../get_network_reachable_vulnerabilities_in_bom.py)
