with signup_date_table as 
(select 
user_id, 
min(login_date) as signup_date 
from user_logins 
group by user_id), 

cte2 as (
select p.user_id, 
s.signup_date as first_login_date, 
count(*) as purchase_count_within_30_days 
from purchases p 
inner join signup_date_table s on 
p.user_id = s.user_id 
where p.purchase_date between 
s.signup_date and s.signup_date + interval 30 day
group by 
p.user_id, first_login_date), 

total_users_ct as (
    select 
    count(distinct user_id) as total_users
    from user_logins), 

total_purchse_user_ct as (
    select 
    count(distinct user_id) as user_purchase_count
    from cte2), 

select round(((select total_users from total_users_ct) /
(select user_purchase_count from total_purchse_user_ct))*100,2)
as conversion_rate;
 
