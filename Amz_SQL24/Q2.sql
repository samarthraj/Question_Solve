with cte1 as (
select 
facility_id, 
sum(energy_consumed_kwh) as total_energy_used_last30 
from 
energy_usage 
where 
energy_type = 'renewable'  
and usage_date > current_date - interval 30 day
group by 
facility_id), 

cte2 as (
select 
facility_id, 
sum(energy_consumed_kwh) as total_energy_used_last30_both 
from 
energy_usage 
where usage_date > current_date - interval 30 day
group by 
facility_id),

cte3 as (
select 
facility_id, 
sum(energy_consumed_kwh) as total_energy_used_lastlast30
from 
energy_usage 
where 
energy_type = 'renewable'  
and usage_date between
current_date - interval 60 day and current_date - interval 30 day
group by 
facility_id), 

cte4 as (
select 
facility_id, 
sum(energy_consumed_kwh) as total_energy_used_lastlast30_both
from 
energy_usage 
where usage_date between
current_date - interval 60 day and current_date - interval 30 day
group by 
facility_id), 

fin_cte as (
select 
cte1.facility_id, 
cte1.total_energy_used_last30,
cte2.total_energy_used_last30_both
cte3.total_energy_used_lastlast30,
cte4.total_energy_used_lastlast30_both
from cte1 inner join 
cte2 on cte1.facility_id = cte2.facility_id 
inner join cte3 on 
cte2.facility_id = cte3.facility_id  
inner join cte4 on 
cte3.facility_id = cte4.facility_id ) 

select 
facility_id, 
round((total_energy_used_last30 * 100) / total_energy_used_last30_both,2) as percentage_last30,
round((total_energy_used_lastlast30 * 100) / total_energy_used_lastlast30_both,2) as percentage_lastlast30 
from fin_cte 
where 
percentage_last30 < percentage_lastlast30






