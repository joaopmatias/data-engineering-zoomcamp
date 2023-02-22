{{ config(materialized='view') }}

select * from {{ source('staging','fhv') }}
limit 100