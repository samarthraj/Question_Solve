with cte as (select 
facility_id, 
report_date, 
carbon_emitted_kg,
lag(carbon_emitted_kg,1) over (partition by facility_id 
order by report_date) as previous_carbon_emitted, 
lag(carbon_emitted_kg,2) over (partition by facility_id 
order by report_date) as previous_previous_carbon_emitted,
lag(report_date,1) over (partition by facility_id 
order by report_date) as previous_date, 
lag(report_date,2) over (partition by facility_id 
order by report_date) as previous_previous_date
from carbon_emissions) 

select 
facility_id, 
report_date as start_report_date, 
previous_previous_date as end_report_date, 
carbon_emitted_kg as start_emission, 
previous_previous_carbon_emitted as end_emission, 
count(*) as number_of_consecutive_increases 
from cte 
where carbon_emitted_kg > previous_carbon_emitted and 
previous_carbon_emitted > previous_previous_carbon_emitted 
group by facility_id
having count(*) >= 3 

