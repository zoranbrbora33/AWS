import json
import os
import boto3

# Initialize AWS clients
s3_client = boto3.client('s3')
dynamodb_client = boto3.client('dynamodb')

# Retrieve the DynamoDB table name from environment variables
dynamodb_table_name = os.environ['DYNAMODB_TABLE_NAME']

def handler(event, context):
    # Get the S3 bucket and object information from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    # Read the JSON file from S3
    response = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
    json_data = response['Body'].read().decode('utf-8')

    # Parse the JSON data
    parsed_data = json.loads(json_data)

    # write data to dynamodb
    dynamodb_client.put_item(
            TableName=dynamodb_table_name,
            Item={
                'id': {'S': parsed_data['id']},
                'value': {'S': parsed_data['value']}
            }
    )