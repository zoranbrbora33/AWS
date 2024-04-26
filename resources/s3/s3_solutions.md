1.  
    Task_1:
        - set the lifecycle rule name

        - checked: Apply to all objects in the bucket

        - checked: Apply to all objects in the bucket 

        - checked: Expire current versions of objects

        - Days after object creation: 1

    For frequently accessed objects it is best to move them to "Standard IA"
    For archive objects that we don"t need fast access it is best to move them
    to Glacier or Glacier Deep Archive

    -- Lifecycle Rules

    Transition Actions - configure objects to transition to another storage class
        - move objects to Standard IA class after set number of days of creation
        - move to Glacier for archiving after set number of days(months)

    Expiration Actions - configure objects to expire after some time
        - access log files can be set for deletion after set number of days
        - can be used to delete old versions of files
        - can be set to delete incomplete multi-part-uploads

    -- Storage Class Analysis
    
    Helps us decide when to transition objects to the right storage class
    Report is updated daily
    24 to 48 hours to start seeing data analysis

2.
    For data that will not be used frequently I would recommend "Glacier Deep Archive".
    Long - lived archive data accessed less than once a year, retreval of data can be long in hours.

3.
    Unit conversions
    S3 Standard storage: 50 TB per month x 1024 GB in a TB = 51200 GB per month
    
    Pricing calculations

    Tiered price for: 51200 GB

    51200 GB x 0.0245000000 USD = 1254.40 USD

    Total tier cost = 1254.4000 USD (S3 Standard storage cost)

    1,000 PUT requests for S3 Standard Storage x 0.0000054 USD per request = 0.0054 USD (S3 Standard PUT requests cost)
        1,254.40 USD + 0.0054 USD = 1,254.41 USD (Total S3 Standard Storage, data requests, S3 select cost)

    S3 Standard cost (monthly): 1,254.41 USD

    S3 Standard cost (upfront): 0.00 USD

4.
    S3 Standard:

    First 50 TB / Month - $0.0245 per GB

    Next 450 TB / Month - $0.0235 per GB

    Over 500 TB / Month - $0.0225 per GB

    S3 Glacier Deep Archive:
    
    All Storage / Month	- $0.0018 per GB

