import boto3
import os
import logging
import sys

logger = logging.getLogger('lambda_sns')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)
 
def lambda_handler(event, context):
    logger.info(f"Event: {event}")
    logger.info(f"Environ: {os.environ['email_topic']}")
    
    sns = boto3.client('sns')
 
    
    response = sns.publish(
        TopicArn=os.environ['email_topic'],    
        Message=str(event),
        Subject="10"
    )