with cte as (select 
user_id, 
login_date, 
lag(login_date, 1) over(partition by 
user_id order by login_date) as last_login_date 
from logins) 

select 
user_id, 
login_date, 
last_login_date, 
datediff(login_date, last_login_date) as days_since_login
from cte 
