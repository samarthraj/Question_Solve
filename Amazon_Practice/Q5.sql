select 
a.user_id, 
a.login_date, 
count(*) as login_counts
from login a 
inner join login b 
on a.user_id = b.user_id 
and 
b.login_date between a.login_date - interval 6 day 
and a.login_date 
group by 
a.user_id, a.login_date

