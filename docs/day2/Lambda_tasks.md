Lambda
Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging. With Lambda, you can run code for virtually any type of application or backend service.

Learning Resources
Lambda:

AWS Lambda Tutorial For Beginners: https://www.youtube.com/watch?v=97q30JjEq9Y 17 min
Documentation: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
Python and Lambda: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html
https://stackify.com/aws-lambda-with-python-a-complete-getting-started-guide/
SQS:

Documentation: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
AWS SQS: https://www.youtube.com/watch?v=vLNDaZuA3Dc 18 min
SNS:

Documentation: https://docs.aws.amazon.com/sns/latest/dg/welcome.html
SNS vs SQS: https://www.youtube.com/watch?v=mXk0MNjlO7A 10 min
CloudWatch Documentation:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
Additional resources
LMS:
AWS Lambda Foundations: https://www.aws.training/Details/eLearning?id=27197
Tasks
Create a Lambda function to ingest IMDb data
Local: resources/lambda/<user>-academy-lambda/lambda_handler.py
AWS Console: <user>-academy-lambda
Timeout: 15 mins
Memory: 1024 MB
Layer: compatible AWS Wrangler
Use global configuration (<username>-academy-global) to iterate over jobs configuration (<username>-academy-jobs) (documentation)
Request API data using jobs configuration
Save response JSON data to s3://<username>-academy-aws/imdb/landing/<table-name>/%Y%m%dT%H%M%S.%f.json (hint: https://www.geeksforgeeks.org/python-convert-string-to-bytes/ and https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object.html; do not user awswrangler - we want to save data as-is, without modifying it oe applying any transformations)
Update jobs configuration to include the latest min_ingestion_dttm (documentation)