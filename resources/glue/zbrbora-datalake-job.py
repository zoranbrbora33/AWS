import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import current_timestamp, current_date

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)



def write_data_to_s3(new_df, table_name):
    glueContext.write_dynamic_frame.from_options(
        frame=new_df,
        connection_type="s3",
        format="glueparquet",
        connection_options={
            "path": f"s3://zbrbora-academy-aws/datalake/{table_name}/",
            "partitionKeys": ["datalake_date"],
        },
        format_options={"compression": "snappy"},
        transformation_ctx="output",
    )


def process_and_store_data(table_name):
    landing_data = glueContext.create_dynamic_frame.from_options(
        format_options={"multiline": False},
        connection_type="s3",
        format="json",
        connection_options={
            "paths": [f"s3://zbrbora-academy-aws/imdb/landing/{table_name}/"],
            "recurse": True,
        },
        transformation_ctx="data",
    )

    df = landing_data.toDF()
    df = df.withColumn("datalake_timestamp", current_timestamp())
    df = df.withColumn("datalake_date", current_date())
    new_df = DynamicFrame.fromDF(df, glueContext, "new_df")

    write_data_to_s3(new_df, table_name)

table_names = ["name_basics", "title_basics", "title_crew", "title_episode", "title_principals", "title_ratings"]


for table_name in table_names:
    process_and_store_data(table_name)

job.commit()
