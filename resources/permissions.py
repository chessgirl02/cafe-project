import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c71268a1429067l3634709t1w861063270874-s3bucket-1s74kkyoz5mvp"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")