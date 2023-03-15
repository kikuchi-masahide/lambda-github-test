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
