-- TASK 1 --
-- Run MSCK REPAIR TABLE `table_name` for all IMDb tables 
-- "MSCK REPAIR TABLE" is used to repair a partitioned table
MSCK REPAIR TABLE `title_ratings`;
MSCK REPAIR TABLE `title_principals`;
MSCK REPAIR TABLE `title_episode`;
MSCK REPAIR TABLE `title_crew`;
MSCK REPAIR TABLE `title_basics`;
MSCK REPAIR TABLE `name_basics`;
