from aws_cdk import Stack, aws_s3 as s3
from constructs import Construct
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3_notifications


class ExampleS3StackStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # created s3 bucket
        bucket = s3.Bucket(self, "zbrbora-academy-s3-cdk", bucket_name="zbrbora-academy-s3-cdk")

        # created dynamoDB table
        table = dynamodb.Table(self, "MyTable",
                               table_name="zbrbora-academy-dynamodb-cdk",
                               partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
                               read_capacity=1,
                               write_capacity=1)
        
        # created lambda function
        lambda_function = _lambda.Function(self, "zbrbora-academy-lambda-cdk",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda.handler", 
            function_name="zbrbora-academy-lambda-cdk",
            code=_lambda.Code.from_asset("lambda_function"),  
        )

        # permission for lambda
        table.grant_write_data(lambda_function)
        bucket.grant_read(lambda_function)
        
        # trigger lambda
        notification = aws_s3_notifications.LambdaDestination(lambda_function)
        notification.bind(self, bucket)

        # trigger for .json files
        bucket.add_object_created_notification(
           notification, s3.NotificationKeyFilter(suffix='.json'))
        
                                           
                                                  
        
