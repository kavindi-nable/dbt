{{config(materialized = 'table', table_name = 'yt_model')}}
SELECT 
    GENRE,    
    COUNT(A) as total
FROM YT
Group BY GENRE