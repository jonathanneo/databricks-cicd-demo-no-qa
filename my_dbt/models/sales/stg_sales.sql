{{ config(materialized='table') }}

select 
    customer_id, 
    customer_name,
    cost
from {{ ref('raw_sales') }}
