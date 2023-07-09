import os
import shutil


# 指定したファイルのLAMBDA_NAMEをnameに置換
def replace_lambda_name(abs_path, name):
    with open(abs_path) as f:
        s = f.read()
        s = s.replace("LAMBDA_NAME", name)
    with open(abs_path, mode="w") as f:
        f.write(s)


# lambda-docker-templateディレクトリの絶対パスを取得
def get_repository_root_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return "/".join(path.split("/")[:-1])


print("lambda名:")
name = input()

root_path = get_repository_root_path()

# github-actionテンプレートのコピー
shutil.copyfile(
    os.path.join(root_path, "lambda/deploy_base_lambda.yml"),
    os.path.join(root_path, ".github/workflows/" + name + ".yml"),
)
# .github/workflows/name.yamlのLAMBDA_NAMEをnameに置換
replace_lambda_name(os.path.join(root_path, ".github/workflows/" + name + ".yml"), name)

# lambda_template.zipをlambda/appに展開し、ディレクトリ名をnameに変更
shutil.unpack_archive(
    os.path.join(root_path, "lambda/lambda_template.zip"),
    os.path.join(root_path, "lambda/app"),
)
os.rename(
    os.path.join(root_path, "lambda/app/lambda_template"),
    os.path.join(root_path, "lambda/app/" + name),
)
lambda_path = os.path.join(root_path, "lambda/app/" + name)
# samconfig.tomlのstack名を置換
replace_lambda_name(os.path.join(lambda_path, "samconfig.toml"), name)
# samテンプレートの関数名の変更
replace_lambda_name(os.path.join(lambda_path, "template.debug.yaml"), name)
replace_lambda_name(os.path.join(lambda_path, "template.deploy.yaml"), name)
