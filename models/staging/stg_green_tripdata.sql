{{ config(materialized='view') }}

select * , 
{{ get_payment_type_description('PUlocationID') }} as pu
from {{ source('staging','fhv') }}
limit 100