AWS Glue
AWS Glue is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.

Learning materials:
AWS Glue documentation: https://docs.aws.amazon.com/glue/
AWS Workflows: https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html
Using AWS Glue to Connect to Data Sources in Amazon S3: https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html
Why to use parquet data format: https://www.upsolver.com/blog/apache-parquet-why-use
Additional materials
A full walk-through: https://towardsdatascience.com/aws-glue-101-all-you-need-to-know-with-a-real-world-example-f34af17b782f
Amazon Web services Lab:AWS Glue step by step part 1: https://www.youtube.com/watch?v=Ol6rl7TqAGY&list=PLDHbO7tw89jRH7qYgjHll3y56wLhjS1Bb&index=3
Amazon Web services Lab:AWS Glue step by step part 2: https://www.youtube.com/watch?v=9V14C0Uy-ZM
Task
Convert s3://<username>-academy-aws/landing/<table-name>/%Y%m%dT%H%M%S.%f.json data to a parquet format and make it available in Athena using Glue Data Catalog and Glue Jobs.

Create two databases in Glue Data Catalog (eu-central-1) (documentation - only follow Step 1)
names:
<username>-academy-aws-landing
<username>-academy-aws-datalake
locations:
s3://<username>-academy-aws/landing
s3://<username>-academy-aws/datalake
descriptions:
iOLAP Academy 2023 - <username> Landing
iOLAP Academy 2023 - <username> Datalake
Create a Glue Crawler that reads through s3://<username>-academy-aws/landing/ and creates tables (title_ratings, name_basics, ...) in Glue Data Catalog (database: <username>-academy-aws-landing) (documentation Use AWS Glue crawlers).

After you've successfully created a table, check if the data in Athena table is correct before you proceed with the next steps.

Create an AWS Glue job (PySpark) that uses a tables that you previously created and write data in parquet format to s3://<username>-academy-aws/datalake/<table-name>.

set the timeout to <= 480min
add 2 new timestamp columns (F.current_timestamp() and F.current_date()) to the datalake table
name the columns as datalake_timestamp and datalake_date, respectively
partition the table by datalake_date.
Create new Glue Crawler that reads through s3://<username>-academy-aws/datalake/ and creates tables (title_ratings, name_basics, ...) in Glue Data Catalog (database: <username>-academy-aws-datalake).

Write some queries and compare runtimes for the .json data table to the newly formatted data in Athena. What are the results and what were your expectations?

Bonus task
Use all the resources that you created in previous tasks and create an AWS Glue workflow that will be triggered on-schedule (daily @ 8AM).

Additional notes
To store the Glue job locally, use the "Script" tab in the AWS Console and copy-paste the code to resources/glue/<user>-academy-glue-datalake/glueetl_datalake.py
Reach out to Danijel Leoni directly or post a message to Teams chat and enjoy the learning process!