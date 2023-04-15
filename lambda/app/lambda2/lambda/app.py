import json
import requests
import os
import boto3

def lambda_handler(event, context):
    try:
        print(event)
        # dynamodbを操作する場合
        # dynamodb = get_dynamodb_client()
        # table = dynamodb.scan(TableName='aws_test')
        # items = table['Items']
        # print(items)

        # s3を操作する場合
        # s3 = get_s3_client()

    except Exception as e:
        print(f'error:{str(e)}')

def get_dynamodb_client():
    # デバッグ時のみ、local dynamodbのクライアントを取得
    if os.environ["debug"] == 'true':
        return boto3.client('dynamodb',endpoint_url='http://localstack.local:4566',region_name="ap-northeast-1")
    return boto3.client('dynamodb')

def get_s3_client():
    # デバッグ時のみ、local dynamodbのクライアントを取得
    if os.environ["debug"] == "true":
        return boto3.client('s3',endpoint_url='http://localstack.local:4566',region_name="ap-northeast-1")
    return boto3.client('s3')
