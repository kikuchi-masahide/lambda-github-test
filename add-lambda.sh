#!/bin/bash

echo "lambda名: "
read name

cp base.yml .github/workflows/$name.yml
sed -i '' "s/FUNCTION_NAME/"$name"/g" .github/workflows/"$name".yml

mkdir app/$name
cd app/$name

touch lambda_function.py
touch requirements.txt