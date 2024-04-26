import json
import boto3

def handler(event, context):
    # Pristupamo S3 objektu iz događaja
    s3_client = boto3.client('s3')
    dynamodb_client = boto3.client('dynamodb')
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Čitamo JSON sadržaj iz S3 objekta
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        json_content = response['Body'].read().decode('utf-8')
        
        # Pretvaramo JSON u Python rječnik
        data = json.loads(json_content)
        
        # Pohranjujemo podatke u DynamoDB tablicu
        dynamodb_client.put_item(
            TableName='zbrbora-academy-dynamodb-cdk',
            Item={
                'id': {'S': data['id']},
                'value': {'S': data['value']}
            }
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }