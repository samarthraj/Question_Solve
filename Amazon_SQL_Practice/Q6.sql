with cte as (select 
user_id, 
login_date, 
lag(login_date, 1) 
over (partition by user_id 
order by login_date asc) as lg_date
from logins) 

date_diff_table as (select 
user_id, 
login_date, 
lg_date, 
datediff(login_date, lg_date) as date_diff 
from cte) 

select 
user_id, 
login_date, 
lg_date as previous_login_date, 
date_diff as days_since_last_login,
case 
    when date_diff <= 15 then 'active' 
    when date_diff > 15 and date_diff <= 30 then 'at_risk' 
    when date_diff > 30 then 'churn_risk' 
    end as churn_status 
from date_diff_table 
