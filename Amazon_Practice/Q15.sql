with cte as (select 
user_id, 
max(login_date) as recent_login_date 
from user_logins 
group by user_id), 

cte2 as (select user_id, 
recent_login_date, 
datediff(current_date, recent_login_date) as previous_gap_days 
from cte)

select user_id, 
recent_login_date, 
previous_gap_days, 
case 
when previous_gap_days >= 15 or previous_gap_days > 30 then 'churn_risk'
else 'active' 
end as churn_risk_flag
from cte2 
