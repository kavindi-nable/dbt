{{config(materialized = 'table', table_name = 'yt_model')}}
SELECT 
    "Genre",    
    COUNT('ID') as total
FROM {{ source('yt_csv', 'yt') }}
Group BY 1