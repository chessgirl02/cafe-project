import boto3
import subprocess

client = boto3.client('lambda', region_name='us-east-1')
ROLE = 'arn:aws:iam::861063270874:role/LambdaAccessToDynamoDB'
BUCKET = subprocess.getoutput('aws s3api list-buckets --query "Buckets[].Name" | grep s3bucket | tr -d "," | xargs')

response = client.create_function(
    FunctionName='get_all_products',
    Runtime='python3.8',
    Role=ROLE,
    Handler='get_all_products_code.lambda_handler',
    Code={
        'S3Bucket': BUCKET,
        'S3Key': 'get_all_products_code.zip'
    }

)

print ("DONE")

