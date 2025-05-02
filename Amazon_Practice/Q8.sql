--buy again 
select 
user_id, 
usage_date 
from feature_usage 
where usage_date between '2023-01-01' and '2023-03-31' 
and feature_usage = 'Buy Again'  
group by user_id
having count(distinct usage_date) >= 10 