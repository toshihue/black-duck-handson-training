# REST APIの疎通確認

## Hubサーバの構築
1. install_swarm.pdf等を参照し、Hubサーバを構築します。

## Hubサーバへの疎通確認
1. ブラウザでhttps://<hub_base_url>/ を開き、ログインし、REST API接続時に使用する認証用のAPI Keyを発行します。
    * 検証用環境は通常自己証明書のエラーが出ますが、許可します。

2. https://www.python.org/downloads/ からPython 3をインストールします。本手順での確認環境では3.7.3です。
    * PCにプログラムをインストールする権限のない方は、[組み込み用Python](#組み込み用Python)を確認してください。
    * 既にPythonを導入済みの方は、``` python --version ```コマンドでPython 2ではなくPython 3であることを確認してください。

3. HTTP通信用モジュールのrequestsをpipでインストールします。

    ```
    pip install requests
    ```
4. 疎通確認スクリプト[rest_api_test.py](rest_api_test.py)をPythonで実行します。
   変数のapi_keyとurlは環境に応じて修正します。

    ```
    python rest_api_test.py
    ```

5. 以下のようにステータスコード200とbearerTokenが表示されれば成功です。

    ```
    <Response [200]>
    "bearerToken":"*************************************",  "expiresInMilliseconds":7199997}
    ```
### 組み込み用Python
1. https://www.python.org/downloads/windows/ から 「Windows x86-64 embeddable zip file」などのポータブル版をダウンロードし、解凍します。
2. https://qiita.com/hirohiro77/items/377dfc0a264acb3db222 等を参考に以下を導入します。
    * pipコマンドの導入
    * pipコマンドでrequestsモジュールを導入

        ```
        <path>\python.exe -m pip install requests
        ```
3. 疎通確認スクリプトを実行します。

    ```
    <path>\python.exe rest_api_test.py
    ```