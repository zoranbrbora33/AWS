AWS Step Functions
AWS Step Functions is a visual workflow service that helps developers use AWS services to build distributed applications, automate processes, orchestrate microservices, and create data and machine learning (ML) pipelines.

Task
Invoke your <user>-academy-lambda Lambda with a Map state over DynamoDB jobs configuration table.

Create a <username>-academy-aws-statemachine Step Function
Create a DynamoDB Scan state and read the jobs configuration table
Create a Map state to perform operations on each item from the Scan state
Invoke your <user>-academy-lambda Lambda and use the Map state output as the Invoke state's input
modify your Lambda to support the provided input
Bonus task
Create a diagram of the workflow you created. Use all the sources (config and data), processes (Lambda, Step Function) and targets (data) in your diagram.

Additional notes
To store the created Step Function definition, use the "Definition" tab in the AWS Console and copy-paste the code to resources/statemachine/definition.json
Reach out to Dario Pleše directly or post a message to Teams chat and enjoy the learning process!
Learning materials:
AWS Step Functions documentation: https://aws.amazon.com/step-functions/
AWS Step Functions Use Cases: https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html
AWS Step Functions Workshop: https://catalog.workshops.aws/stepfunctions/en-US/
Iterate a DynamoDB table with AWS StepFunctions: https://halftome.medium.com/iterate-a-dynamodb-table-with-aws-stepfunctions-ce0bb9512114