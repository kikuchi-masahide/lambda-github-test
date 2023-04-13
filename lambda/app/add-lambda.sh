#!/bin/bash

echo "lambda名: "
read name

# github-actionテンプレートのコピー
cp base.yml "../workflows/$name.yml"
sed -i "s/FUNCTION_NAME/"$name"/g" "../workflows/$name.yml"

mkdir $name
cd $name

# テンプレートのコピー
unzip ../template.zip
#stack名の変更
sed -i "s/aws-sam-example/$name/g" samconfig.toml