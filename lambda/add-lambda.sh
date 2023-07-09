#!/bin/bash

echo "lambda名: "
read name

# github-actionテンプレートのコピー
cp deploy_base_lambda.yml "../.github/workflows/$name.yml"
cd ../.github/workflows
sed -i "" "s/FUNCTION_NAME/${name}/g" $name.yml
cd ../../lambda/app

# aws samテンプレートのコピー
mkdir $name
cd $name
unzip ../../lambda_template.zip -d .
# stack名の変更
sed -i "" "s/FUNCTION_NAME/$name/g" samconfig.toml
# 関数名の変更
sed -i "" "s/FUNCTION_NAME/$name/g" template.debug.yaml
sed -i "" "s/FUNCTION_NAME/$name/g" template.deploy.yaml
