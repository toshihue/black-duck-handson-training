# スニペットマッチコンポーネントの手動追加
## 概要
スニペットマッチしたコンポーネントの脆弱性情報を表示させるために、スニペットマッチしたコンポーネントと同じコンポーネントをREST APIで「手動で追加」します。


## 課題
スニペットマッチしたコンポーネントと同じコンポーネントを「手動で追加」(Manually Added)します。
* スニペットスキャンをしたプロジェクトとプロジェクトバージョンは画面UI等で確認し、固定で与えるものとします。
* 事前にSwaggerで"GET /api/projects/{projectId}/versions/{projectVersionId}/components (findBomComponentsV2)"の結果を確認します。
* スニペットマッチしたコンポーネントだけでフィルタする方法を確認します。
    * コンポーネントのフィルタ一覧はこちらで、こちらから使用するフィルタのFilter KeyとFilter Valueを確認します。
```
adjusted
bomAttribution
bomComponents
bomComponentSource
bomInclusion
bomLicense
bomMatchReviewStatus
bomMatchType
bomPolicy
bomReviewStatus
bomUsage
cryptoAlgorithms
customSignature
licenseRisk
policyRuleSeverity
policyRuleViolation
securityRisk
```

* Swaggerで追加時のリクエストデータのフォーマットを確認します。APIから自動で追加したことが記録に残るよう、コメントとして「変更」(Component Modification)にその旨を自動で記載します。


### テンプレート

```add_snippet_matched_components_in_bom.py
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

if get_component_response.ok:

    # Code here
    for item in get_component_data['items']:
        # Code here

        else:
            print('Error Message:', add_component_response.text)

else:
    print('Error Message:', get_component_response.text)
    sys.exit(1)


```

* 解答例の方法では既存の「変更」は上書きされてしまうことに注意してください。

### 解答例
[解答例](../add_snippet_matched_components_in_bom.py)
