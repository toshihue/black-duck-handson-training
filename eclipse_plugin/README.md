# Eclipse Plugin
Black Duckで提供しているIDEプラグインは、[Black Duck Eclipse Plugin](https://synopsys.atlassian.net/wiki/spaces/INTDOCS/pages/622869/Black+Duck+Eclipse+Plugin) と[Black Duck Visual Studio Plugin](https://synopsys.atlassian.net/wiki/spaces/INTDOCS/pages/622923/Black+Duck+Visual+Studio+Plugin)です。（2019年6月現在）

OSSのソフトウェアコンポジション解析(SCA)をシフトレフトするために、最も早期に解析を実施ためのツールの一つとして、IDEプラグインを活用できます。

本トレーニングでは、Black Duck Eclipse Pluginの実際に利用する手順を紹介します。

## 対応パッケージマネージャ
* Maven
* Gradle

    ※いわゆるシグネチャスキャンは行われません。

## 表示項目
* コンポーネント名
* コンポーネントバージョン
* コンポーネントのライセンス
* コンポーネントの脆弱性数（高リスクの降順表示）


## 参考資料
公式マニュアルは[Black Duck Eclipse Plugin](https://synopsys.atlassian.net/wiki/spaces/INTDOCS/pages/622869/Black+Duck+Eclipse+Plugin)にあります。

## 事前準備
1. Neon 4.6以降のEclipseをインストールします。（インストールセットはEclipse IDE for Java Developersなど）
2. [Black Duck Eclipse Plugin](https://synopsys.atlassian.net/wiki/spaces/INTDOCS/pages/622869/Black+Duck+Eclipse+Plugin)にしたがって以下を実施します。 
    * 「To download and install the Black Duck Eclipse plugin」を参照し、Black Duck Eclipse pluginをインストールします。
        * Eclipse Marketplaceから Black Duckの検索をしても表示されない場合は、[Help] -> [Install New Software...]より、[Work With:]に https://blackducksoftware.github.io/hub-eclipse-plugin/ を入力し、下のツリーから[Black Duck]を選択し、インストールしてください。
    * インストール後、Eclipseの再起動が求められます。
    * 再起動後、「To configure the Eclipse plugin」を参照し、以下のHubへの接続情報を入力し、[Test Connection]ボタンをクリックし、Hubサーバとの接続確認をします。
        * Username
        * Password
        * Instance URL
        * Always Trust Server Certificate（自己証明書の場合はTrue）
        * Proxy設定（各ネットワーク環境に応じて設定します）
    

## EclipseでSCAの実施

### GithubからMavenプロジェクトをClone
ここではGithubで公開されているsprint-petclinicというSpringベースのWebアプリケーションのリポジトリを解析します。
1. [File] -> [Import]
2. [Git] -> [Project from Git], [Next>]
3. [Clone URI], [Next>]
4. [URL]:"https://github.com/spring-projects/spring-petclinic.git" , [Next>]
5. [Directory]:必要に応じて変更, [Next>]
6. [Next>]
7. [Import using the New Project wizard], [Finish]
8. [Cancel]（うまくMavenプロジェクトとしてインポートできないので、一旦キャンセル）

### EclipseにMavenプロジェクトとしてインポート
1. [File] -> [Import]
2. [Maven] -> [Existing Maven Projects], [Next>]
3. [Root Directory]: <Githubからのチェックアウト先のPath>, [Finish]
4. Welcomタブを閉じる

### Black Duckによる解析
1. インポートしたsprint-petclinicプロジェクトで右クリックします。
2. [Black Duck] -> [Open Component Inspector] で、解析結果を表示します。
    * 自動で解析が始まらない場合は、 [Black Duck] -> [Inspect Selected Project] で解析します。

## トレーニング
### Lab 1
中リスクの脆弱性を含むjQueryの脆弱性を解消してください。

[解答例](answer)

