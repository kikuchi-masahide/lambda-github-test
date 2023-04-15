import boto3

dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:4566",region_name="ap-northeast-1")

aws_test = dynamodb.create_table(
    TableName="aws_test",
    KeySchema=[{
        'AttributeName': 'id',
        'KeyType': 'HASH'
    }],
    AttributeDefinitions=[{
        'AttributeName': 'id',
        'AttributeType': 'S'
    }],
    BillingMode='PAY_PER_REQUEST'
)

items = [
    {
        "id": "0",
        "name": "a"
    },{
        "id": "1",
        "name": "b"
    }
]

with aws_test.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)