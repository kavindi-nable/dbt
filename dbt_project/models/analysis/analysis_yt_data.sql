{{ config( materialized='table', table_name='analysis_yt_data' ) }}

SELECT
    GENRE,
    COUNT(A) as total,
    MAX(A) as maximum,
    MIN(A) as minimum, 
    AVG(A) as average
    
FROM YT
GROUP BY GENRE
