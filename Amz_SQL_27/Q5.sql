with cte as (select 
facility_id, 
report_month,
solar_energy_generated_kwh, 
lag(solar_energy_generated_kwh, 1) 
over(partition by facility_id order by report_month) as 
previous_month_solar_energy 
from solar_energy_reports), 

cte2 as (select 
facility_id, 
report_month,
solar_energy_generated_kwh, 
round(((previous_month_solar_energy - solar_energy_generated_kwh) * 100
/ previous_month_solar_energy),2) as energy_percentage
from 
cte) 

select 
facility_id, 
report_month,
solar_energy_generated_kwh, 
energy_percentage, 
case 
    when energy_percentage > 70 then 'yes' 
    else 'no'
    end as anomaly
from cte2 


