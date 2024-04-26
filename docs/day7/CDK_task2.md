AWS CDK Day 2
Task summary
Today's task is creating a custom CDK application from scratch. It will include multiple AWS resources which interact with each other in one way or another.

Task details
The application you will create needs to be able to receive a JSON file, read its content, and persist it in DynamoDB. The file structure is standardized and defined below.

File structure
{
    "id": "string" ,
    "value": "string"
}
Resources
Main resources you will need are:

S3 Bucket (used to receive a file)
Lambda Function (used to parse the file and write to DynamoDB)
DynamoDB Table (used to persist the record)
As you progress through this task you will find that in order to enable these resources to work together you will also grant privileges so these resources can function in conjunction.

Hints
Use the S3 Bucket Event Notifications to invoke the Lambda Function
Naming conventions
Stacks: <user>-cdk-stack-task-2
Buckets: <user>-academy-s3-cdk
Lambda: <user>-academy-lambda-cdk
DynamoDB: <user>-academy-dynamodb-cdk