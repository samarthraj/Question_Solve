with cte as (
select user_id, 
sum(total_amount) as total_spent 
from orders 
group by 
user_id) 

select user_id, 
total_spent, 
case 
    when total_spent > 1000 then 'High Value'
    when total_spent >= 500 and total_spent <= 1000 then 'Medium value' 
    when total_spent < 500 then 'Low Value'  
    end as value_segment 
from cte 

