
with cte as (select 
facility_id, 
date_trunc('month',report_date) as report_month
from water_usage_reports 
where 
report_date >= current_date - interval 1 year) 

cte2 as (select 
facility_id,
count(distinct report_month) as months_reported_last_6_months 
from cte 
where report_month >= current_date - interval 6 month 
group by 
facility_id
having count(distinct report_month) = 6) 

select 
facility_id,months_reported_last_6_months from cte2