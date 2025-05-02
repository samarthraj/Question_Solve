select 
f.facility_id,
f.recycling_reported_kg,
r.expected_recycling_kg 
from 
facility_waste_reports f 
left join 
recycling_standards r 
on f.facility_id = r.facility_id
where 
f.recycling_reported_kg < r.expected_recycling_kg
or f.recycling_reported_kg IS NULL  