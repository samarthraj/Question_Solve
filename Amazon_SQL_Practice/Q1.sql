--users 
--logins 
--orders 

with cte as (select u.user_id, 
max(l.login_date) as recent_login
from 
users u 
inner join logins l 
on u.user_id = l.user_id 
where u.is_prime = 'True' 
group by u.user_id
having 
max(l.login_date) < current_date - interval 30 day) 

cte2 as (select 
cte.user_id, 
cte.recent_login, 
o.order_date, 
o.actual_delivery_date, 
o.expected_delivery_date
from cte 
inner join orders o 
on o.user_id = cte.user_id 
where o.order_date between 
current_date - interval 3 month 
and current_date 
group by cte.user_id, cte.recent_login, 
o.order_date, 
o.actual_delivery_date, 
o.expected_delivery_date
having count(order_id) >= 1) 

with cte3 as (select 
user_id, 
max(recent_login) as most_recent_login, 
max(order_date) as recent_order_date,  
count(
    case when actual_delivery_date > expected_delivery_date then 1 
    end
) as late_delivery_counts
from cte2 
group by 
user_id) 


select 
cte3.user_id, 
ct3.most_recent_login, 
login_date







