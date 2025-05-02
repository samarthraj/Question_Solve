with cte as (
select 
customer_id, 
date_format(order_date, '%Y-%m') as order_month, 
date_format(lead(order_date) over (partition by 
customer_id order by order_date), '%Y-%m') 
as next_order_month
from orders 
where order_date between 
current_date - interval 4 month and 
current_date), 

cte2 as (
    select order_month as month, 
    count(distinct customer_id) as customer_this_month
    from cte 
    group by order_month
),

cte3 as (
    select order_month as month, 
    count(distinct customer_id) as customer_next_month
    from cte 
    where next_order_month is not null 
    and next_order_month != order_month
    group by order_month
)

select cte2.month, 
cte2.customer_this_month, 
cte3.customer_next_month 
from cte2 inner join cte3 on 
cte2.month = cte3.month 



