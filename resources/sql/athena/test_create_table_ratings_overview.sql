-- TASK 2 --
CREATE TABLE rating_overview AS
SELECT
  rating_range,
  COUNT(*) AS title_count,
  SUM(CAST(numvotes AS INT)) AS total_votes
FROM (
  SELECT
    CASE
     WHEN "average_rating" >= 0 AND "average_rating" < 1 THEN '0-1'
     WHEN "average_rating" >= 1 AND "average_rating" < 2 THEN '1-2'
     WHEN "average_rating" >= 2 AND "average_rating" < 3 THEN '2-3'
     WHEN "average_rating" >= 3 AND "average_rating" < 4 THEN '3-4'
     WHEN "average_rating" >= 4 AND "average_rating" < 5 THEN '4-5'
     WHEN "average_rating" >= 5 AND "average_rating" < 6 THEN '5-6'
     WHEN "average_rating" >= 6 AND "average_rating" < 7 THEN '6-7'
     WHEN "average_rating" >= 7 AND "average_rating" < 8 THEN '7-8'
     WHEN "average_rating" >= 8 AND "average_rating" < 9 THEN '8-9'
     WHEN "average_rating" >= 9 AND "average_rating" <= 10 THEN '9-10'
     ELSE NULL
    END AS rating_range,
    CAST(numvotes AS INT) AS numvotes
  FROM (
    SELECT
      CAST(averagerating AS DOUBLE) AS average_rating,
      numvotes
    FROM title_ratings
  ) AS subquery
) AS subquery
GROUP BY rating_range
ORDER BY rating_range;