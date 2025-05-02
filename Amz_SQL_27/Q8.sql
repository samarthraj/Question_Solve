with cte as (select 
i.facility_id, 
i.region,
date_trunc('month', e.report_date) as months
sum(e.energy_consumed_kwh) as total_energy
from 
facility_info i inner join 
facility_energy_reports e 
on i.facility_id = e.facility_id 
where 
e.report_date >= current_date - interval 6 month 
group by 
i.facility_id, 
i.region, date_trunc('month', e.report_date))  

select 
region, 
months,
avg(total_energy) as avg_energy_consumed_per_active_facility 
from cte
group by 
region, months;



