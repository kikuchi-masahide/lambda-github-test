import os
import boto3


# AWSのクライアントを取得(s3 = get_aws_client("s3")のように使用)
def get_aws_client(service_name):
    # デバッグ時のみ、localstackのクライアントを取得
    if os.environ.get("debug") == "true":
        return boto3.client(
            service_name,
            endpoint_url="http://localstack.local:4566",
            region_name="ap-northeast-1",
        )
    return boto3.client(service_name)
