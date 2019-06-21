# 脆弱性の個数集計
## 概要
UI画面では各レベルの脆弱性を含む「コンポーネント数」の内訳しか表示されないため、REST APIを利用してリスクレベル別の「脆弱性の数」を集計する。

## 課題
プロジェクトバージョン内のリスクレベル別の「脆弱性の数」を集計する。


### テンプレート

```count_vulnerabilities_in_bom.py
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

# Code here



```


### 解答例
[解答例](../count_vulnerabilities_in_bom.py)
