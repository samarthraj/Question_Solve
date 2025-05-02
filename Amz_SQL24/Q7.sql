
with cte as (select 
facility_id, 
report_date, 
carbon_emitted_kg, 
lag(carbon_emitted_kg, 1) 
over (partition by facility_id order by report_date) 
as previous_emission_kg from 
carbon_emissions) , 

cte2 as (select 
facility_id, 
report_date, 
carbon_emitted_kg, 
previous_emission_kg, 
round(((carbon_emitted_kg - previous_emission_kg)*100/previous_emission_kg),2) 
as percentage_change 
from cte), 

cte3 as (
select
facility_id, 
report_date, 
carbon_emitted_kg, 
previous_emission_kg, 
percentage_change,
row_number() over(partition by facility_id 
order by report_date desc) as rn 
from cte2 
where percentage_change > 50) 

select 
facility_id, 
report_date, 
carbon_emitted_kg, 
previous_emission_kg, 
percentage_change,
rnk 
from 
cte3 
where rn = 1 