# REST API
以下のようなユースケースにおいて、REST APIを活用すると便利です。
* Hubの画面UIでの反復作業の自動化をしたい
* データの集計、整形をしたい
* 画面UIでは、デフォルトで表示されている内容（脆弱性の表示スコア、件数など）調整したい
* Project/Version -> Component/Version -> Vulnerability のような参照をして一覧化したい

## トレーニング一覧
||内容|
|:-------| :--- |
|[Lab0](Lab0)|REST APIの疎通確認|
|[Lab1](Lab1)|認証APIの理解|
|[Lab2](Lab2)|ユーザの作成|
|[Lab3](Lab3)|ユーザの読み取り|
|[Lab4](Lab3)|グループの作成|
|[Lab5](Lab3)|グループへのロール割当|
|[Lab6](Lab3)|グループへのユーザ割当|
|[Lab7](Lab3)|スニペットマッチコンポーネントの手動追加|
|[Lab8](Lab3)|脆弱性の個数集計|
|[Lab9](Lab3)|ネットワーク経由で攻撃可能な脆弱性一覧表示|

## サポートされるエンドポイント
以下のいずれかの条件に合致するエンドポイントはInternal APIであるため、予告なしに変更される可能性があります。そのため原則は使用不可です。
* Pathに"/internal"を含む
* Pathが"/v1"から開始する
* Media Type(ResponseのContent Type)に"internal" を使用している

## Media Type
* Media Typeはなにか(V)
    * Toavoidissues,whensendingorreceivingdata,specifytheBlackDuckmediatypeintheAcceptheader.

## 参考資料

|名前|入手場所|内容|
| :------- | :--- | :--- |
|Black Duck REST API|https://<hub_base_url>/api-doc/public.html | 2019.6.0よりBeta公開の新APIドキュメント。RequestとResponseの実例が最も充実しています。サポート対象のPublic APIのみを掲載しています。一方で掲載APIの網羅率は低いです。（2019年6月現在）。認証APIはこちらの記載の方法を推奨します。| |
|REST API Developers Guide |https://<hub_base_url>/api.html | 旧Swagger APIドキュメント。APIの網羅度は高いです。filterのKeyとValueなどパラーメータの具体例が読み取れないケースが多いです。Swaggerで生成しているためか、Internal APIも含まれているため要注意。 | |
|HUB REST API Python bindings|https://github.com/blackducksoftware/hub-rest-api-python| Synopsysのソリューションアーキテクトが公開している利用シーン別にパッケージ化したPythonプログラムです。APIの使い方が不明な場合に具体例として参考になります。モジュール化しているため、読み解く際には元のAPIのEndpointとの対応付けはしづらいです。Internal APIも使用されているため要注意です。製品ではないのでサポート対象ではありません。|
|Getting Started with the SDK|https://community.synopsys.com/s/synopsys-user-guides|認証から実データの取得までの簡単なチュートリアルの記載があります。各種認証の方法の記載もありますが基本は参照不要です。|
|ネットワークキャプチャ|ブラウザで「Ctrl + Shift + I」（Chrome、Firefox） |具体的なパラーメータが不明な場合は、画面UIでの操作結果を観察するのが現状は早道です。|

## REST API vs Report Database

||REST API|Report Database|
| :---- | :--- | :--- |
|リアルタイム性|リアルタイム|15分毎に反映|
|情報量|画面UIよりは劣る|一部のみ|
|データの更新|可能|参照のみ|
|データの結合|jsonデータの扱いが必要のため、煩雑|SQLによる結合が可能|
|データの集計|filterやsearchでデータを絞ることが可能。大量のデータが返却される場合は、limitパラメータで制限する必要がある。jsonを再帰的に読み取り集計する必要がある。|SQLによる集計が可能|
|構造的データの扱い|扱いやすい|扱いにくい|
|外部公開|API Keyによる認証が可能。ユーザのロール、API Key R/Wを生成時に指定できるため、より安全に管理可能。|IDとパスワードのによる認証であり、DBのポートを直接開放するため、外部公開向きではない。|
|難易度|RESTful APIとjsonデータに馴染みが必要。初めは認証部分がハードルになる。|SQLの知識があればすぐに使用できる。|
