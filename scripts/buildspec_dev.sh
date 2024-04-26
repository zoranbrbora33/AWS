export S3_STACK_NAME="zbrbora-academy-stack-s3"
export DataS3BucketName="zbrbora-academy-data"
export ScriptsS3BucketName="zbrbora-academy-scripts"
export OWNER_NAME="zbrbora-zoranbrbora1717@gmail.com"

export DYNAMODB_STACK_NAME="zbrbora-academy-dynamodb-stack"
export DYNAMODB_TABLE_GLOBAL="zbrbora-academy-cicd-global"
export DYNAMODB_TABLE_JOBS="zbrbora-academy-cicd-jobs"

aws cloudformation deploy \
    --template-file cicd/s3.yml \
    --stack-name $S3_STACK_NAME \
    --parameter-overrides \
        DataS3BucketName=$DataS3BucketName \
        ScriptsS3BucketName=$ScriptsS3BucketName \
    --tags Owner=$OWNER_NAME

aws cloudformation deploy \
        --template-file cicd/dynamodb.yml \
        --stack-name $DYNAMODB_STACK_NAME\
        --parameter-overrides \
          DynamoDBTableGlobalName=$DYNAMODB_TABLE_GLOBAL \
          DynamoDBTableJobsName=$DYNAMODB_TABLE_JOBS \
        --tags Owner=$OWNER_NAME



- export STATE_MACHINE_STACK_NAME="zbrbora-academy-statemachine-stack"
- export STATE_MACHINE_NAME="zbrbora-academy-statemachine-cicd"
- export STATE_MACHINE_TRIGGER_ROLE_NAME="zbrbora-statemachine-trigger-role-cicd"

- export LAMBDA_FUNCTION_NAME="zbrbora-academy-lambda"
- export LAMBDA_FUNCTION_ROLE_NAME="zbrbora-lambda-role-cicd"

- echo "===================== State Machine Deployment Start ====================="
      - >
        aws cloudformation deploy \
          --template-file cicd/statemachine.yml \
          --stack-name $STATE_MACHINE_STACK_NAME \
          --parameter-overrides \
            S3BucketData=$DATA_S3_BUCKET_NAME \
            S3BucketScripts=$SCRIPTS_S3_BUCKET_NAME \
            DynamoDBTableGlobalName=$DYNAMODB_TABLE_GLOBAL \
            DynamoDBTableJobsName=$DYNAMODB_TABLE_JOBS \
            StateMachineName=$STATE_MACHINE_NAME \
            StateMachineRoleName=$STATE_MACHINE_ROLE_NAME \
            StateMachineTriggerRoleName=$STATE_MACHINE_TRIGGER_ROLE_NAME \
            LambdaLandingName=$LAMBDA_FUNCTION_NAME \
            LambdaLandingRoleName=$LAMBDA_FUNCTION_ROLE_NAME \
          --tags Owner=$OWNER_NAME
- echo "===================== State Machine Deployment Complete ====================="


- export LAMBDA_STACK_NAME="zbrbora-academy-lambda-stack"
- export LAMBDA_FUNCTION_NAME="zbrbora-academy-lambda-cicd"

- echo "===================== Lambda Deployment Start ====================="
      - >
        aws cloudformation deploy \
          --template-file cicd/lambda.yml \
          --stack-name $LAMBDA_STACK_NAME \
          --parameter-overrides \
            LambdaFunctionName=$LAMBDA_FUNCTION_NAME \
          --tags Owner=$OWNER_NAME
- echo "===================== Lambda Deployment Complete ====================="


Resources:
  StateMachineRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Ref StateMachineRoleName
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: states.amazonaws.com
            Action: sts:AssumeRole

  StateMachine:
    Type: AWS::StepFunctions::StateMachine
    Properties:
      StateMachineName: !Ref StateMachineName
      RoleArn: !GetAtt StateMachineRole.Arn
      DefinitionString:
        Fn::Sub: |
              {
                "Comment": "DynamoDB Scan",
                "StartAt": "Scan",
                "States": {
                  "Scan": {
                    "Type": "Task",
                    "Resource": "arn:aws:states:::aws-sdk:dynamodb:scan",
                    "Parameters": {
                      "TableName": "zbrbora-academy-jobs"
                    },
                    "Next": "ProcessAllItems"
                  },
                  "ProcessAllItems": {
                    "Type": "Map",
                    "ItemsPath": "$.Items",
                    "ResultPath": "$.mappedResults",
                    "Iterator": {
                      "StartAt": "ProcessItem",
                      "States": {
                        "ProcessItem": {
                          "Type": "Task",
                          "Resource": "arn:aws:lambda:eu-central-1:456582705970:function:zbrbora-academy-lambda",
                          "End": true
                        }
                      }
                    },
                    "End": true
                  }
                }
              }



AWSTemplateFormatVersion: "2010-09-09"

Parameters:
  S3BucketData:
    Type: String
  S3BucketScripts:
    Type: String
  DynamoDBTableGlobalName:
    Type: String
  DynamoDBTableJobsName:
    Type: String
  StateMachineName:
    Type: String
  StateMachineRoleName:
    Type: String

- echo "===================== Statemachine Deployment Start ====================="
      - >
        aws cloudformation deploy \
          --stack-name $STATE_MACHINE_STACK_NAME \
          --template-file cicd/statemachine.yml \
          --force-upload \
          --parameter-overrides \
            S3BucketData=$DATA_S3_BUCKET_NAME \
            S3BucketScripts=$SCRIPTS_S3_BUCKET_NAME \
            DynamoDBTableGlobalName=$DYNAMODB_TABLE_GLOBAL \
            DynamoDBTableJobsName=$DYNAMODB_TABLE_JOBS
            StateMachineName=$STATE_MACHINE_NAME \
            StateMachineRoleName=$STATE_MACHINE_ROLE_NAME \
          --no-fail-on-empty-changeset \
          --capabilities CAPABILITY_NAMED_IAM \
          --tags Owner=$OWNER_NAME
      - echo "===================== Statemachine Deployment Complete ====================="

