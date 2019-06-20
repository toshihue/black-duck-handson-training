# Report Database
* Blak Duckの解析結果に関するデータを出力します。
    * SQL等が利用できるため、決まった集計を載せるレポートの作成をする際に活用できます。
* 15分に一回"ReportingDatabaseTransferJob"ジョブにより、Hub内部で使用するテーブルより、一部の情報をReport Databaseにコピーします。

## 参考資料
* Report Database (ファイル名：<hub_version>_report_database.pdf)
* [Black Duck Reporting Database](https://synopsys.atlassian.net/wiki/spaces/BDLM/pages/65765948/Black+Duck+Reporting+Database)

## 接続情報
デフォルトの接続情報は、[Black Duck Reporting Database](https://synopsys.atlassian.net/wiki/spaces/BDLM/pages/65765948/Black+Duck+Reporting+Database)を参照ください。

## テーブル、カラム名
<hub_version>_report_database.pdf を参照。

## 開放ポートの変更方法
Report Database用の待受ポートをデフォルトの55436から変更するには、docker-compose.ymlの修正もしくはdocker-compose.local-overrides.ymlへの追記をし、コンテナの再起動をしてください。
以下はポートを80番に変更した例です。
```docker-compose.local-overrides.yml
services:
  postgres:
    ports: ['80:5432']
```

# 事前準備
https://community.synopsys.com/s/synopsys-user-guides よりReport Databaseのマニュアルを入手します。
## Excelによる疎通確認
1. マニュアルの「Chapter 2: Using Excel with the report database」より ODBC driverをWindowsに設定し、ExcelよりReport Databaseに接続してください。
    * WindowsのODBC Driverの具体的なURLはこちら： https://ftp.postgresql.org/pub/odbc/versions/msi/psqlodbc_09_06_0500.zip
        * ODBC Driverのbitは、インストールしているExcelのbitに合わせる必要があります。
    * 「Configuring data source credentials」の手順で、PostgresSQL35W等のデータソースが表示されない場合は、「Extracting data from the report database」の手順から進めると表示されることがあります。

2. Projectテーブルに画面UIで表示されるプロジェクト一覧のレコードが表示できれば成功です。

## PgAdminによる疎通確認
1. https://www.pgadmin.org/download/ よりPgAdmin 4をダウンロードし、インストールします。
2. [Excelによる疎通確認](#Excelによる疎通確認)と同じ要領で接続情報を入力し、接続します。
3. Projectテーブルに画面UIで表示されるプロジェクト一覧のレコードが表示できれば成功です。


# トレーニング
## Lab 0
以下のテーブルのデータをExcelで表示し、どのようなカラムがあるか確認してください。
* Project Table
* Project Version Table
* Component Table
* Component License Table
* Component Vulnerability Table

## Lab 1
OpenSSLのHub上のコンポーネントIDを確認し、使用されているOpenSSLの全バージョンを表示してください。

[解答例](Lab1.sql)


## Lab 2
ライセンス名に"GNU"が含まれるコンポーネント一覧について、id(Component Table)、コンポーネント名、コンポーネントバージョン、ライセンス名を表示してください。
ヒント：Component Table、Component License Table、INNER JOIN

[解答例](Lab2.sql)

## Lab 3
プロジェクトバージョンごとの中以上のセキュリティリスクかつ未対応の数を集計してください。
ヒント：project_versionテーブル、projectテーブル、componentテーブル、component_vulnerabilityテーブル、INNER JOIN

[解答例](Lab3.sql)


## 注意点
* 現状は、REST APIに比べると取得できる情報は少ないです。Report Databaseからのデータ取得を採用する前に、テーブルとカラムを確認し、取得したいデータが取得できるか確認をお願いします。
* 未ConfirmedのSnippetマッチコンポーネントも、Component TableやComponent Vulnerability Tableに表示されます。
* 大量なスキャン（マッチング）を一度に実施した場合には、15分以上経っても"ReportingDatabaseTransferJob"が終わらないことがあります。その場合はジョブ一覧で状況を確認してください。
* Component Match Type Tableがなぜか空です。

