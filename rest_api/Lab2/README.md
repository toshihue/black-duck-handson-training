# ユーザの作成
## 概要
多数のUserを新規作成して、Black Duck上のProjectに割り当てる場合、手動で実施するのが現実的ではありません。
Groupを使用したアクセス権管理をする場合、一般的に以下の流れになることが多いはずです。

1. Projectの作成 
2. Groupの作成
3. GroupのGlobal Roleへの割当
4. GroupのProjectとProject Roleへの割当
5. Userの作成
6. UserのGroupへの割当

本ハンズオンでは「1.Project」以外のところを一通り触れていきます。
ここで作成したユーザを以降のハンズオンでも使用したいのと、一番分かりやすいAPIであるため、「5. Userの作成」から開始します。

## 一般的にREST APIで必要な情報
* HTTPメソッド
* エンドポイントのURLのPath
* Headerの指定
    * Content-Type（Response形式の指定）
    * Accept (RequestのData形式の指定)
* Data(json)
* Parameter
* Response形式(json)

## 課題
上記の必要な情報を意識して、ユーザを一つ作成してください。

### テンプレート

```create_user.py
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

# Creating a User
user_response_data_format = # Code here
user_request_data_format = # Code here
user_request_headers = {

}

url_path = # Code here
user_name = # Code here
first_name = # Code here
last_name = # Code here
email = # Code here
active = # Code here
password = # Code here

user_request_data = {
    # Code here
}

user_request_json = json.dumps(user_request_data).encode('utf-8')
user_response = requests.post(# Code here)
print(datetime.datetime.now(), os.path.basename(__file__) + ':', user_response)
if user_response.ok:
    user_response_json = user_response.json()
    # formatted_json = json.dumps(user_response_json, indent=2)
    # print(formatted_json)
    print('Created User Name:', user_name)

else:
    print('Error Message:', user_response.text)
```
* requests.urllib3.disable_warnings()でverify=Falseへの警告がでないようにします。
* 認証はLab1で確認した認証モジュールを使用します。
* base_url、verify、api_keyも都度修正を避けるため、config.iniファイルから読み取ります。
* pythonのdictionary型であるuser_request_dataをjson化するためにjson.dumps()を使用します。
* user_response.okによる判定で、簡易的にHTTP200番台と300番台を処理成功とします。
* リクエスト失敗時は、レスポンスの本文を出力するために、user_response.textを表示します。

### 解答例
[create_user.py](../create_user.py)