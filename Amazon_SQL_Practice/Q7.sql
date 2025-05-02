select 
user_id, 
feature_name,
count(feature_name) as feature_ct
from feature_usage
where usage_date between '2023-01-01' and '2023-03-31' 
and feature_name = 'Buy Again' 
group by user_id, 
feature_name
having count(feature_name) >= 10 



