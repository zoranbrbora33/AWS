-- TASK 3 --
CREATE VIEW title_insights AS
SELECT *, 
    max_start_year - min_start_year AS year_diff,
    max_runtime_minutes - min_runtime_minutes AS runtime_diff
FROM 
    (SELECT DISTINCT "titletype",
        MAX(CAST(startyear AS INT)) AS max_start_year,
        MIN(CAST(startyear AS INT)) AS min_start_year,
        MAX(CAST(runtimeminutes AS INT)) AS max_runtime_minutes,
        MIN(CAST(runtimeminutes AS INT)) AS min_runtime_minutes
    FROM title_basics
    WHERE "primarytitle" = "originaltitle"
        AND "startyear" != '\N' AND "runtimeminutes" != '\N'
    GROUP BY "titletype"
    LIMIT 5);