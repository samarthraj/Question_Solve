--atleast 3 orders in total 
--but none in the last 90 days 
with cte as (
select user_id, 
count(order_id) as total_orders 
max(order_date) as last_order_date
from 
orders 
group by user_id
having count(order_id) >= 3
and max(order_date) < current_date - interval 90 day
) 

select u.user_id, 
u.name, cte.last_order_date, 
cte.total_orders from users u 
inner join cte on cte.user_id = u.user_id


