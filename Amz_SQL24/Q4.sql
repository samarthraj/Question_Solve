select 
sg.panel_id, 
avg(sg.energy_generated_kwh) as avg_energy_generated, 
ss.capacity_kwh_per_day, 
count(sg.generation_date) as no_of_days
from solar_generation sg
inner join 
solar_specs ss
on ss.panel_id = sg.panel_id 
where sg.generation_date > current_date - interval 30 day
group by 
sg.panel_id
having avg(sg.energy_generated_kwh) < (0.6 * ss.capacity_kwh_per_day)



