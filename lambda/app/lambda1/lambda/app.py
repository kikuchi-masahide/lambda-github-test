import json
import requests

def lambda_handler(event, context):
    try:
        print(event)
        print('lambda1')
    except Exception as e:
        print(f'error:{str(e)}')

