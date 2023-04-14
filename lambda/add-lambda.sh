#!/bin/bash

echo "lambda名: "
read name

# github-actionテンプレートのコピー
cp base.yml "../.github/workflows/$name.yml"
cd ../.github/workflows
sed -i "" "s/FUNCTION_NAME/${name}/g" $name.yml
cd ../../lambda/app

# aws samテンプレートのコピー
mkdir $name
cd $name
unzip ../../template.zip -d .
#stack名の変更
sed -i "" "s/aws-sam-example/$name/g" samconfig.toml