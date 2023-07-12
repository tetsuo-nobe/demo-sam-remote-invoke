import boto3
import uuid
import os
from botocore.config import Config
from aws_xray_sdk.core import patch
patch(['boto3'])

def lambda_handler(event, context):
    print(event)
    #
    table = os.getenv('DDB_TABLE')
    id = str(uuid.uuid4()) 
    fname = event['first_name']
    lname = event['last_name']
    message = "Hello! " + fname + " " + lname 
    #
    client = boto3.client('dynamodb')
    item = {
           "user_id": {"S": id},
           "first_name": {"S": fname},
           "last_name": {"S": lname},
    }
    client.put_item(TableName=table, Item=item)
    #
    return {
        "statusCode": 200,
        "body": message
    }
