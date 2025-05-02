with cte as (
select 
facility_id, 
sum(carbon_emitted_kg) as total_carbon_emitted_kg_per_facility, 
sum(units_processed) as total_units_processed_per_facility 
from 
carbon_emissions 
where report_date > current_date - interval 30 day
group by 
facility_id), 

cte2 as (select 
facility_id,
round(total_carbon_emitted_kg_per_facility
/total_units_processed_per_facility,2) as avg_emission_per_facility
from cte),  

cte3 as (select 
sum(total_carbon_emitted_kg_per_facility) as global_c, 
sum(total_units_processed_per_facility) as global_u
from cte ) 

select 
facility_id, 
avg_emission_per_facility 
from cte2 
where 
avg_emission_per_facility > 
(select (round(global_c/global_u,2)) from cte3)
order by avg_emission_per_facility desc 
limit 3 