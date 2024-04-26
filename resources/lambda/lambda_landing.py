import boto3
import requests
import json
import datetime

def lambda_handler(event, context):

    table_name = event['table_name']['S']
    last_ingest = json.loads(event['params']['S'])
    
    s3_client = boto3.client('s3')

    dynamodb = boto3.resource('dynamodb')

    global_table = 'zbrbora-academy-cicd-global'
    global_table = dynamodb.Table(global_table)
    global_response = global_table.scan()

    jobs_table = 'zbrbora-academy-cicd-jobs'
    jobs_table = dynamodb.Table(jobs_table)
    jobs_response = jobs_table.scan()

    method = global_response["Items"][0]["method"]
    host = global_response["Items"][0]["host"]
    prefix = global_response["Items"][0]["prefix"]
    rest_api_url = f"{method}{host}/{prefix}"
    
    try:
        
        partitions_endpoint = f"/partitions/{table_name}"
        response = requests.get(rest_api_url + partitions_endpoint, params=last_ingest)
        partitions = response.json()
    
        for partition in partitions:

            try:
                
                data_endpoint = f"/dataset/{table_name}?min_ingestion_dttm={partition}"
                response = requests.get(rest_api_url + data_endpoint)
                data = response.json()
                
                now = datetime.datetime.now()
                timestamp_str = now.strftime("%Y%m%dT%H%M%S.%f")
                #s3_key = f'imdb/landing/{table_name}/{timestamp_str}.json'
                s3_key = f'imdb/landing/{table_name}/{partition}.json'
                
                s3_client.put_object(Body=data, Bucket='zbrbora-academy-data', Key=s3_key)
               

                print(f"Table: {table_name} - New partition: {partition}")
                
                new_min_ingestion_dttm = partition  
                last_ingest["min_ingestion_dttm"] = new_min_ingestion_dttm
                
                jobs_table.update_item(
                    Key={"table_name": table_name},  
                    UpdateExpression="SET params = :new_params",
                    ExpressionAttributeValues={":new_params": json.dumps(last_ingest)}
                )
               
            except ValueError:
                print(f"{table_name} - partition {partition} can\"t be uploaded cause it is probably damaged!!!")
                    
            print(f"CHECK: Table: {table_name} - New partition: {partition}")


        success_message = "Lambda function executed successfully."
        publish_notification_to_sns(success_message)
        
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        publish_notification_to_sns(error_message)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def publish_notification_to_sns(error_message):
    sns_client = boto3.client('sns')
    topic_arn = "arn:aws:sns:eu-central-1:456582705970:zbrbora-academy-sns-lambda"
    sns_client.publish(TopicArn=topic_arn, Message=error_message, Subject="Lambda Notification")