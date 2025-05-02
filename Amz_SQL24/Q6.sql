with cte as (select 
facility_id, 
max(report_date) as last_report_date 
from carbon_emissions 
group by facility_id 
having 
max(report_date) < current_date - interval 30 day), 

cte3 as (select count(distinct facility_id) as faci_count_below30 
from cte),

cte2 as 
(select 
count(distinct facility_id) as faci_ct 
from carbon_emissions)  


select round((select faci_count_below30 from cte3)*100/ 
(select faci_ct from cte2), 2) as percentage_faci;

