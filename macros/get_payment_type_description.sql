 {#
    This macro returns the description of the payment_type 
#}

{% macro get_payment_type_description(payment_type) -%}

    case when {{ payment_type }} between 0 and 50 then 'less than 50'
    when {{ payment_type }} between 51 and 100 then 'greater than 50'
    else 'greater than 100'
    end

{%- endmacro %}