Amazon Redshift
Learning resources:
https://aws.amazon.com/redshift/
Getting started with Amazon Redshift: https://www.youtube.com/watch?v=dfo4J5ZhlKI 50 min
Deep dive on best practices for Amazon Redshift: https://www.youtube.com/watch?v=13iIj34nkQE 30 min
Getting started with Amazon Redshift Spectrum: https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html
Additional resources
LMS: AWS Databases - Basic:
Amazon RDS Service Introduction: https://www.aws.training/Details/Video?id=36900
Amazon Redshift Service Primer: https://www.aws.training/Details/eLearning?id=36901
Tasks
Expose the ingested IMDb data as Redshift tables. DBMS tools:

DBeaver Community
AWS Redshift query editor v2
Credentials: iOLAP AWS Redshift Cluster. Mentors will provide the password.
Create an S3 External Schema imdb_redshift_db.<username>_academy_imdb
Define an external schema in Redshift that references the S3 bucket containing the IMDb datalake data.
Create Redshift Spectrum Tables
Define Redshift Spectrum tables for all IMDb data based on the datalake tables
Use Athena queries from SQL course on Spectrum tables and compare Redshift-Athena performance for the same queries