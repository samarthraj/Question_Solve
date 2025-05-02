-- within 14 days of its release.

with cte as feature_usage_cte as (select 
u.user_id, 
u.feature_name,
f.release_date, 
u.usage_date 
from features f inner join 
feature_usage u on 
f.feature_name = u.feature_name),  

cte2 as (select 
count(distinct user_id) as 
user_count_in_first_14_days,  
feature_name
from feature_usage_cte 
where usage_date between 
release_date and 
release_date + interval 14 day
group by feature_name ), 

ranked_table as (select 
user_count_in_first_14_days,  
feature_name, 
dense_rank() over(order by user_count_in_first_14_days
desc) as rnk 
from cte2) 

select feature_name 
from ranked_table where rnk = 1



