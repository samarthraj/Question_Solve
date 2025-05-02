with cte as (select 
f.order_id, 
o.region, 
f.frustration_score,
case 
    when o.actual_delivery_date <= o.expected_delivery_date then 'on_time'
    when o.actual_delivery_date > o.expected_delivery_date then 'late' 
    end as delivery_status 
from orders o 
inner join feedback f 
on f.order_id = o.order_id) 

select 
region, 
delivery_status, 
avg(frustration_score) as score 
from cte 
group by region, delivery_status
order by region, delivery_status


