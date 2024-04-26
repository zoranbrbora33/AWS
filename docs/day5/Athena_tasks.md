Amazon Athena
Learning resources:
https://aws.amazon.com/athena/
An introduction to Amazon Athena: https://www.youtube.com/watch?v=nib_-3llYTA
Athena deep dive: https://www.youtube.com/watch?v=tzoXRRCVmIQ
Additional resources
Introduction to Amazon Athena: https://www.aws.training/Details/Video?id=15885
Tasks
Perform Data Analysis with Athena: Write SQL queries in Athena to analyze the IMDB data. Use the queries created in the SQL course. Record the execution time for each query.

Run MSCK REPAIR TABLE `table_name` for all IMDb tables
Utilizing conditional expressions on the <username>-academy-imdb-datalake.imdb_title_ratings table do the following:
Create ranges per each full rating over the averagerating values
e.g. Values like 2.3, 2.4, 2.7 should fall into the 2-3 range while similarly values like 5.4, 5.6 and 5.7 should fall into the 5-6 range
For each rating range count the number of titles and the sum of total votes
Once your query is done create another table in your schema utilizing CTAS (CVAS)
Name the table: <username>-academy-imdb-datalake.ratings_overview
In your database, utilizing window functions on the <username>-academy-imdb-datalake.title_basics do the following:
Select 5 different title types
For each title type filter out min and max values for start_year run_time_minutes columns where primary title and original title are the same for their respective types.
Once you have min year and max start_year values in a separate column calculate the number of years between them. What does this result column show?
Similarly, for the first and last run_time_minutes values calculate the difference between last and first value.
This should be done in one query, in order to do so, please utilize subqueries
Once your query is done create another view in your schema utilizing CVAS
Name the table: <username>-academy-imdb-datalake.title_insights