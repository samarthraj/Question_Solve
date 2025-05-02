--3*avg(usage) last 30 days 
with cte as (
select 
facility_id, 
avg(water_consumed_liters) as avg_usage 
from water_usage 
where 
usage_date > current_date - interval 30 day 
group by 
facility_id)

select 
cte.facility_id, 
cte.avg_usage,
w.water_consumed_liters,
w.usage_date
from cte 
inner join water_usage w
on cte.facility_id = w.facility_id 
where 
w.usage_date > current_date - interval 30 day 
having 
w.water_consumed_liters > (3*cte.avg_usage)





