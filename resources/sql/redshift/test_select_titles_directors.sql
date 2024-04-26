-- athena runtime -> Run time: 5.28 sec
-- redshift runtime -> Elapsed time: 4.388 sec
SELECT primarytitle AS title, directors 
FROM zbrbora_academy_imdb.title_crew AS tc
INNER JOIN zbrbora_academy_imdb.title_basics AS tb
ON tb.tconst = tc.tconst
WHERE directors != '\N';

