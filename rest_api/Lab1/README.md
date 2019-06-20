# 認証APIの理解
## 概要
API Keyで認証後し、後続する通常のREST APIの呼び出しで必要なBearer Tokenを取得します。
個々のAPI Keyが仮に漏洩しても、そのKeyを無効化することで不正アクセスへの対応がしやすいため、API Keyによる認証を推奨します。

## Black Duck REST APIでのリクエスト、レスポンス例
### リクエスト
API Keyによる認証
```
POST /tokens/authenticate HTTP/1.1
Authorization: token [API token]
Accept: application/vnd.blackducksoftware.user-4+json
```

### レスポンス
bearerTokenとその有効時間（二時間後）の返却
```response.json
{
  "bearerToken" : "[bearer token]",
  "expiresInMilliseconds" : 10000
}
```

### 後続のREST APIで渡すHTTPヘッダ(Bearer Token)
```
Authorization: Bearer [bearer token]
```

## curlコマンドでの実施
リクエストコマンド
```
curl -X POST --header 'Authorization: token xxxxxxx' 'Accept: application/vnd.blackducksoftware.user-4+json' -i https://<hub_base_url>/api/tokens/authenticate --insecure
```
* -X POST: HTTP POSTメソッド
* --header 
    * 'Authorization: token xxxxxxx': HTTPヘッダに API Key をセット
    * 'Accept: application/vnd.blackducksoftware.user-4+json' : レスポンス用のMedia Typeの指定
* -i: リクエスト先のURL
* --insecure: 自己証明書のため、証明書を信頼するオプション

## Python 3での実装例　

```rest_api_auth.py
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
```
環境に依存する以下の3つの変数を引数とします。
* base_url: API呼び出し対象HubサーバURLのベース部分
* api_key: API呼び出しをするユーザのAPI Key 
* verify: 自己証明書かどうか(自己証明の場合はFalseを渡す)

レスポンスをjsonデータとして扱うことで、bearer_tokenの取り出しが楽であることが分かります。

以降、REST APIのハンズオンにおいて、上記を[認証用モジュール](../api_test.py)として活用します。