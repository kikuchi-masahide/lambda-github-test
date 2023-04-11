#!/bin/bash

echo "lambda名: "
read name

mkdir $name
cd $name

# テンプレートのコピー
unzip ../template.zip
#stack名の変更
sed -i "s/aws-sam-example/$name/g" samconfig.toml