import boto3

s3 = boto3.client('s3',endpoint_url="http://localhost:4566",region_name="ap-northeast-1")

s3.create_bucket(
    Bucket='s3-test-geelive',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-northeast-1'
    }
)

s3.upload_file(
    './mnt/test.txt',
    's3-test-geelive',
    'test.txt'
)
