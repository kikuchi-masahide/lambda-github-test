import json
import requests
import os
import boto3

def lambda_handler(event, context):
    try:
        print(event)
        dynamodb = get_dynamodb_client()
        table = dynamodb.scan(TableName='aws_test')
        items = table['Items']
        print(items)

    except Exception as e:
        print(f'error:{str(e)}')

def get_dynamodb_client():
    # デバッグ時のみ、local dynamodbのクライアントを取得
    if os.environ["debug"] == 'true':
        return boto3.client('dynamodb',endpoint_url='http://dynamodb:8000')
    return boto3.client('dynamodb')