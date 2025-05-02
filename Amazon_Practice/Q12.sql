with cte as (select 
user_id as active_user, 
date_format(login_date, '%Y-%m') as 
this_month, 
lead(date_format(login_date, '%Y-%m')) over (
    partition by user_id order by date_format(login_date, '%Y-%m') 
) as next_month
from logins),  

cte2 as (select 
count(distinct user_id) as active_users_this_month, 
this_month 
from cte 
group by this_month), 

cte3 as (select 
count(distinct user_id) as active_users_next_month, 
next_month 
from cte 
where next_month is not Null 
and next_month != this_month
group by this_month) 

select 
cte2.this_month, 
cte2.active_users_this_month, 
cte3.active_users_next_month 
from cte2 left join cte3 on 
cte2.this_month = cte3.next_month 



