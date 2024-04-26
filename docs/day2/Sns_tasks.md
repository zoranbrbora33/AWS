SNS
Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers). Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel. Clients can subscribe to the SNS topic and receive published messages using a supported endpoint type, such as Amazon Kinesis Data Firehose, Amazon SQS, AWS Lambda, HTTP, email, mobile push notifications, and mobile text messages (SMS).

Learning Resources
SNS:

Documentation: https://docs.aws.amazon.com/sns/latest/dg/welcome.html
SNS vs SQS: https://www.youtube.com/watch?v=mXk0MNjlO7A 10 min
Create an SNS topic <user>-academy-sns-lambda:

# resources/sns/<user>-academy-sns-lambda.json
Type: "AWS::SNS::Topic"
Properties:
    TopicName: "<user>-academy-sns-lambda"
Create a new Lambda function (<user>-academy-lambda-sns-test) that will read messages from an event:

{
    "message": "Hello from SNS!"
}
and send that message to your email using SNS. Sometimes confirmation mail can be sent to the spam or junk folder, so make sure to check those

Modify your <user>-academy-lambda Lambda function so that in case of a Lambda error, that error is sent to your email using SNS (wrap try/except over lambda_handler)

Additional notes
Reach out to Danijel Leoni directly or post a message to Teams chat and enjoy the learning process!