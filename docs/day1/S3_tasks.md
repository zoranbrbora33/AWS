# Amazon Simple Storage Service

Amazon Simple Storage Service (Amazon S3) is storage for the internet.
You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.

## Learning resources:
* https://docs.aws.amazon.com/s3/index.html?nc2=h_ql_doc_s3
* https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
* AWS Storage Services: https://www.youtube.com/watch?v=cF1Zc7KrhLQ [55 min]
* Getting started with Amazon S3: https://www.youtube.com/watch?v=vFfY_-TL-pc [50 min]

* Choose one video of your preference

## Additional resources

* AWS Storage Offerings: https://www.aws.training/Details/eLearning?id=39246


## Task - Introduction

Create a new S3 bucket in the console and name it `<username>-s3-task`. Upload one JSON file in prefix `files/`. [1] Find out what is the best practice to delete objects from the bucket and implement it on created prefix so the data is deleted 1 day after coming to a bucket. 
   - let's say that you have a process that puts sensitive data from some source system to your bucket
   - after some time, you notice that incoming data is not accessed frequently. Only data in the last three months is accessed
   - you have 50 TB (20,000,000,000 files) of data older than that - you don't want to lose it, but you want to archive it for future use
   - [2] Based on your research, which S3 Storage class would you recommend for keeping the data that will not be used frequently and doesn't request frequent access?
   - [3] Calculate the cost of transferring files to that Storage class from S3 Standard. 
   - [4] What is the cost of keeping the data in S3 Standard and the one from your previous answer?

Document and explain [1, 2, 3, 4] to `S3_solutions.md`.

## Task - Prerequisite for upcoming development

Create an S3 bucket ([documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)):
   - name: `<username>-academy-aws`
   - region: `eu-central-1`
   - tag: `Owner = <your-email>`
   - other options can be left unchanged

## Additional notes

* Reach out to Danijel Leoni directly or post a message to Teams chat and enjoy the learning process!
