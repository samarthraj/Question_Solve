with cte as (select 
count(distinct user_id) as count_ids, 
event_type 
from events 
group by event_type ) 

cte2 as (select 
event_type, 
count_ids, 
lag(count_ids, 1) over (order by
case 
when 'view' then 1 
when 'add_to_cart' then 2
when 'purchase' then 3
end 
) as lg_counts 
from cte) 

select 
event_type, 
count_ids, 
round((lg_counts / count_ids) * 100, 2) as conversion_rate_from_previous 
from cte2 
