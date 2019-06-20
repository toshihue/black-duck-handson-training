# 解答
1. Hub UI画面の検索でjQueryの脆弱性情報を確認し、既知の脆弱性がないバージョンを調査します。
2. sprint-petclinicディレクトリ直下のpom.xmlの`<webjars-jquery.version>` タグの値を以下のように修正し、保存します。再度Black Duckの解析を実行します。
    ```
        <webjars-bootstrap.version>3.3.6</webjars-bootstrap.version>
        <webjars-jquery-ui.version>1.11.4</webjars-jquery-ui.version>
        <webjars-jquery.version>3.4.1</webjars-jquery.version>

    ```
実際には、jquery 3.4.1が現在のアプリで使用している機能の範囲で互換があるかどうかを確認した上で、修正を検討します。
