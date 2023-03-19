## コンテナ操作について

### コンテナ起動
```
./docker-start.sh
```

### コンテナに接続
```
./docker-login.sh
```

### コンテナ終了
```
./docker-stop.sh
```


### パッケージインストール方法
コンテナにログインし下記を実行
```
pip3 install -t . -r requirements.txt
```

### lambdaにアップロードするzipファイル生成方法(app.zip)
ホストPCで下記を実行
```
./zip.sh
```

### 留意事項
いずれかのコマンドが実行できない場合、chmod 755 ./~~~.shを行う

## Github Actionsについて

Github Actionsのsecretsを設定することにより、mainブランチにpushしたコードをlambdaへdeployすることができる

### deploy対象

appフォルダ

requirements.txt内のパッケージもgithub actions上で一時的にインストールされ、自動でアップロードされる

### 必要な設定

1. AWSユーザのアクセスキーID、シークレットアクセスキー作成。
2. Github Actinosのsecrets設定。以下の表のように設定する

|  Name  |  Secret  |
|-------|-------|
|  AWS_ACCESS_KEY_ID  |  アクセスキーID  |
|  AWS_SECRET_ACCESS_KEY  |  シークレットアクセスキー  |
|  FUNCTION_NAME  |  lambda関数名  |
