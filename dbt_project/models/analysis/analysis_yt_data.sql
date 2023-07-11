{{ config( materialized='table', table_name='analysis_yt_data' ) }}

SELECT
    (SELECT COUNT(*) FROM {{ ref('yt_model') }}) AS total_count,
    (SELECT AVG(total) FROM {{ ref('yt_model') }}) AS mean,
    (SELECT MIN(total) FROM {{ ref('yt_model') }}) AS min_value,
    (SELECT MAX(total) FROM {{ ref('yt_model') }}) AS max_value

    
FROM {{ ref('yt_model') }}
GROUP BY 1
