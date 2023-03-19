#github-action-test
import requests

def lambda_handler(event, context):
    # テストサイトにGETを投げてみる
    response = requests.get('https://httpbin.org/get', params={'foo': 'bar'})
    return response.json()
