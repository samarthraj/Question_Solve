--feature_usage(user_id, feature_name, usage_date)

select 
user_id, 
usage_date, 
count(distinct feature_name) as feature_count 
from feature_usage  
group by 
user_id, 
usage_date 
having 
count(distinct feature_name) >= 3 