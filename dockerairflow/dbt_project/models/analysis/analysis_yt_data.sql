{{ config( materialized='table', table_name='analysis_yt_data' ) }}

SELECT
    GENRE,
    COUNT(ID) as total,
    MAX(ID) as maximum,
    MIN(ID) as minimum, 
    AVG(ID) as average,
    STDDEV(ID) as standardDeviation
    
FROM YT
GROUP BY GENRE
