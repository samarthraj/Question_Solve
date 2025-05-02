select 
u.user_id, 
u.name
from users u 
left join 
orders o 
on u.user_id = o.user_id 
and 
o.order_date >= 
current_date - interval 90 day 
where o.order_id is Null
AND u.user_id IN (
      SELECT user_id FROM orders
  );
