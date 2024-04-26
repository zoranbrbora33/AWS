import json
import boto3

def lambda_handler(event, context):
    sns_topic_arn = 'arn:aws:sns:eu-central-1:456582705970:zbrbora-academy-sns-lambda'
    email_subject = 'Message from SNS'
    email_body = event['message']

    sns_client = boto3.client('sns', region_name='eu-central-1')

    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Subject=email_subject,
        Message=email_body
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully')
    }

