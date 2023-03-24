{{ config( materialized='table', table_name='analysis_yt_data' ) }}
SELECT CHANNEL_NAME, SUBSCRIBER_COUNT
FROM yt_data
ORDER BY SUBSCRIBER_COUNT
LIMIT 10