# Dynamo DB

Using DynamoDB to store data ingestion and jobs configurations, you can maintain the metadata and settings required for the ETL process. DynamoDB offers fast and scalable performance, allowing you to retrieve and update configurations efficiently.

## Learning Resources
* AWS Documentation: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
* AWS DynamoDB Tutorial:
  * https://www.youtube.com/watch?v=k0fcbRj_pZE [30 min]
  * https://www.youtube.com/watch?v=2mVR_Qgx_RU [10 min]


## Additional resources
* Amazon DynamoDB Service Introduction: https://www.aws.training/Details/Video?id=36857
* Amazon DynamoDB Service Primer: https://www.aws.training/Details/eLearning?id=36858
* Amazon DynamoDB – Architecture and Features: https://www.aws.training/Details/eLearning?id=50877

## Tasks

1. Create a DynamoDB table (`<user>-academy-global`) to store global data ingestion configuration.
  - table schema:

    ```yml
    # resources/dynamodb/tables/<user>-academy-global.json
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: "<user>-academy-global"
      AttributeDefinitions:
        - AttributeName: "name"
          AttributeType: "S"
        - AttributeName: "tz"
          AttributeType: "S"
        - AttributeName: "method"
          AttributeType: "S"
        - AttributeName: "host"
          AttributeType: "S"
        - AttributeName: "port"
          AttributeType: "S"
        - AttributeName: "prefix"
          AttributeType: "S"
        - AttributeName: "url"
          AttributeType: "S"
        - AttributeName: "partitions_uri"
          AttributeType: "S"
        - AttributeName: "content_type"
          AttributeType: "S"
      KeySchema:
        - AttributeName: name
          KeyType: HASH
      ProvisionedThroughput:
          ReadCapacityUnits: 1
          WriteCapacityUnits: 1

    ```

2. Add an item to the table

  ```json
  // resources/dynamodb/items/<user>-academy-global.json
  {
    "name": "imdb-rest-api",
    "tz": "Europe/Zagreb",
    "method": "https://",
    "host": "ogj9fvz5cf.execute-api.eu-central-1.amazonaws.com",
    "port": "",
    "prefix": "v1/imdb",
    "url": "{method}{host}{port}/{prefix}",
    "partitions_uri": "/partitions/{table_name}",
    "jobs": "[\"title_ratings\",\"title_crew\",\"name_basics\",\"title_episode\",\"title_basics\",\"title_principals\"]"
  }
  ```

3. Design a new `<user>-academy-jobs` DynamoDB table to store *jobs configuration* (hint: `<user>-academy-python`).
  - create the table
  - populate the table with *items*

