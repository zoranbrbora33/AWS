import json
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

def handler(event, context):
    S3_BUCKET = 'zbrbora-academy-scripts'
    S3_KEY_GLOBAL = 'dynamodb/items/zbrbora-academy-imdb-global.json'
    DYNAMODB_TABLE_GLOBAL = 'zbrbora-academy-cicd-global'

    S3_KEY_JOBS = 'dynamodb/items/zbrbora-academy-imdb-jobs.json'
    DYNAMODB_TABLE_JOBS = 'zbrbora-academy-cicd-jobs'

    response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY_GLOBAL)
    json_data = json.loads(response['Body'].read().decode('utf-8'))

    for item in json_data:
      dynamodb.put_item(
        TableName=DYNAMODB_TABLE_GLOBAL,
        Item={
          'name': {'S': item['name']},
          'tz': {'S': item['tz']},
          'method': {'S': item['method']},
          'host': {'S': item['host']},
          'port': {'S': item['port']},
          'prefix': {'S': item['prefix']},
          'url': {'S': item['url']},
          'partitions_uri': {'S': item['partitions_uri']},
          'content_type': {'S': item['content_type']}
      }
    )

    response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY_JOBS)
    json_data = json.loads(response['Body'].read().decode('utf-8'))

    for item in json_data:
      table_name = item['table_name']

      dynamodb.put_item(
        TableName=DYNAMODB_TABLE_JOBS,
        Item={
          'table_name': {'S': table_name},
          'uri': {'S': item['uri']},
          'params': {'S': item['params']}
        }
      )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda!!!')
    }

    