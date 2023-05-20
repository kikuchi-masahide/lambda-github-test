## 基本的な使い方について

### 初回のみの操作

- aws samのインストール。pip3,brewなど
- `./docker-rebuild.sh`

### デバッグの開始

- localstackの起動。
    - docker(localstack)を起動:`./docker-start.sh`
    - `./docker-login.sh`
    - dynamodb、S3をローカルで起動する場合、ディレクトリを変更せずに
        ```python3 table_setup.py```

        ```python3 s3_setup.py```

        等を実行

        dynamodb、S3等と連携しないラムダの場合、この手順は不要
    
    - parameter storeの設定。```./parameter-store.sh```を実行。

- コンテナにログインせずに`./debug.sh -s (デバッグするラムダ名)`<br/>
lambdaに渡すイベント(エントリポイントの引数event)を指定する場合、`-e`オプションでjsonを指定。`-e events/test.json`など。

環境変数を使用する場合、template.debug.yamlに追記する。具体的には、以下のようにEnvironmentの部分を追記
```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function 
    Properties:
      ...
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
      Environment:
        Variables:
          debug: "true"
          KEY1: "VALUE1"
          KEY2: "VALUE2"
```

### 管理するラムダを追加したい

awsに作成済みのラムダは現状おそらく不可

新規のラムダの場合、`./add-lambda.sh`を実行、lambda名を入力

コード本体は、lambda/app/(lambda名)/lambda/app.py

IAMポリシーのアタッチ、トリガーの設定はブラウザから行わなければいけないため注意

### ラムダを削除したい

`aws sam delete --stack_name (ラムダ名)`を実行。

ゴミが残る可能性があるので、ブラウザでラムダのみを削除は良くなさそう。

### ./~~.shで'Permission denied'のようなエラーが出た時

`chmod 755 ~~.sh`

## Github Actionsについて

Github Actionsのsecretsを設定することにより、mainブランチへpushした変更をクラウドに適用できる

### 必要な設定

1. AWSユーザのアクセスキーID、シークレットアクセスキー作成。
2. Github Actinosのsecrets設定。以下の表のように設定する

|  Name  |  Secret  |
|-------|-------|
|  AWS_ACCESS_KEY_ID  |  アクセスキーID  |
|  AWS_SECRET_ACCESS_KEY  |  シークレットアクセスキー  |
|  PACKAGE_S3_BUCKET  |  samのデータ保存等に用いるS3バケット  |

## ファイル構成について

(わかるファイル/フォルダのみ)

- .github/workflows
    - (lambda名).yml:github actionのフロー。
- lambda
    - app
        - (lambda名)
            - .aws-sam:sam buildの生産物 .gitignoreする
            - events:lambdaのエントリポイントに渡すデータ。`./debug.sh`の`-e`オプションで指定
            - lambda
                - app.py:コード本体。ラムダ全体のエントリポイントは`lambda_handler(event,context)`
                - requirements.txt:aws側で標準で持っていないパッケージを使う際、必要なパッケージを列挙する。
            - samconfig.toml:sam関係の設定。`stack_name`のみ変更
            - template.debug.yaml,template.deploy.yaml:デバッグ時、デプロイ時に用いる、cloudfront的なデータ
    - localstack
        - mnt:localstackのコンテナとバインドしているディレクトリ。S3にファイルをアップロードしたい時は、このフォルダに入れておけばコンテナ内でも使用可能
        - s3_setup.py,table_setup.py:s3,dynamodbのセットアップ用のコード。なんとなくファイルを分けているが1つにまとめても問題ない。書き方の注意は下に。
    - add-lambda.sh
    - base.yml:ラムダを追加するとき使う、github action用のテンプレート
    - debug.sh
    - docker-compose.yaml
    - docker-login.sh:localstackのコンテナへのログイン用
    - docker-rebuild.sh
    - docker-start.sh
    - docker-stop.sh
    - template.zip:ラムダを追加する時用の雛形


## s3_setup.pyとtable_setup.pyを書くときの注意

デフォルトのコードにあるように、`boto3.client`や`boto3.resource`を用いる際は、<u>引数の`endpoint_url`を指定する</u>
```
s3 = boto3.client('s3',endpoint_url="http://localhost:4566",region_name="ap-northeast-1")
```
エンドポイントを指定し、コンテナのlocalstackに繋がるようにする

## samとlocalstack周りについて備忘録

localstack:<br/>
awsの挙動をローカルで再現するモック。かなり幅広く再現できそう<br/>
https://localstack.cloud/

- docker-compose.yamlでコンテナを立てる
- ネットワークcontainer-linkは、localstackとsamのデバッグコンテナで共有。ref. debug.sh
- Dockerfile内でdynamodb/S3のセットアップも行いたかったが、何故か怒られるので断念
- template.<u>debug</u>.yamlとtemplate.<u>deploy</u>.yamlの違いは、API GATEWAYを作るか否か。API GATEWAYがないとsam local invokeが動かなくなる。
- stackについていまいちよくわかっていないので、1ラムダ1スタックで管理。スタック名はラムダ名と共通に。

## 今後やることについて

- 細かい変更:
    - s3_setup.py、table_setup.pyをDockerfileで実行するように
    - stack関係について。全ラムダを1スタックで管理するようにするとどうなるのか?スタックごと一括削除になるのか?
    - localstackのデータの永続化。
- awsリソースの管理自体について:
    - samの使用を継続する場合:<br/>
    dynamodb,S3,ec等はcloudformationで管理、lambdaはsamで管理<br/>
    cloudformationとsamの書き方はほぼ共通のようなので、cloudformationを知るとラムダの管理も楽そう
    - samをlocalstackで代用する場合<br/>
    全リソースをcloudformationで作成/管理<br/>
    localstackでlambdaとcloudformationも扱えるため、デバッグがそちらで可能。コンテナを1つ立ててログインしデバッグするだけなので、クライアント側でaws-cliなどのインストールが不要。