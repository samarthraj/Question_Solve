with cte as (select 
f.facility_id, 
f.region,
sum(w.water_used_liters) as total_water 
from 
facility_info f left join 
water_usage_reports w 
on f.facility_id = w.facility_id 
where 
w.report_date >= current_date - interval 6 month
group by 
f.facility_id, f.region), 

select 
region, 
sum(total_water) as total_water_used, 
avg(total_water) as avg_water_per_facility 
from cte 
group by 
region





