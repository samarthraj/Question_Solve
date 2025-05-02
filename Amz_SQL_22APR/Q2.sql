with all_user_logins_per_month as (select 
user_id, 
date_format(login_date, '%Y-%m') as month_date 
from user_logins) 

(select 
month_date, 
count(*) as active_login_counts_per_month 
from all_user_logins_per_month 
group by month_date) 

