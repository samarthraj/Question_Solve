with cte1 as (select 
user_id, 
login_date,
lag(login_date, 1) over (partition by 
user_id order by login_date asc) as lag_date 
from logins), 

cu as (select 
user_id, 
login_date as reactivation_login,
lag_date as last_login_before_churn, 
datediff(login_date, lag_date) as diff_date
from cte1 
where 
datediff(login_date, lag_date) >= 30) 

select 
cu.user_id, 
cu.reactivation_login, 
datediff(p.purchase_date, cu.reactivation_login) as day_number, 
sum(p.amount) as rolling_30day_total
from cu left join purchases p 
on p.user_id = cu.user_id 
where p.purchase_date between 
cu.reactivation_login and cu.reactivation_login + interval 30 day
group by 
cu.user_id,
cu.reactivation_login





