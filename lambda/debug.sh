#!/bin/bash

# オプションの初期化
stack=""
ev=""

# オプションの処理
while getopts :s:e: optKey; do
  case "$optKey" in
    s)
      stack="$OPTARG"
      ;;
    e)
      ev="$OPTARG"
      ;;
    \?)
      echo "無効なオプション: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "オプションが引数を必要としています: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

# -stackオプションが必須なので、値がセットされているかチェック
if [ -z "$stack" ]; then
  echo "-stackオプションは必須です。"
  exit 1
fi

# cdコマンドでディレクトリを移動
cd "app/$stack"

# sam buildコマンドを実行
sam build --use-container -t template.debug.yaml --skip-pull-image

# -eオプションが付与されていれば、オプション値を変数evに受け取り、sam local invoke -eを実行
if [ -n "$ev" ]; then
  sam local invoke --docker-network localstack.internal --parameter-overrides debug=true -e "$ev"
else
  # -eオプションが付与されていなければ、sam local invokeを実行
  sam local invoke --docker-network localstack.internal --parameter-overrides debug=true
fi