
with company_count as (select 
aviacompany, 
count(*) as company_count 
from flights 
group by aviacompany), 

destination_ct as (select 
aviacompany,
destination 
count(destination) as destination_ct, 
from flights 
group by 
aviacompany,
destination) 

select 
f.id, 
f.destination, 
f.departure_time 
from flights f 
inner join company_count
on f.aviacompany = company_count.aviacompany 
inner join destination_ct 
on company_count.aviacompany = destination_ct.aviacompany
and f.destination = destination_ct.destination 
order by 
company_count desc, 
aviacompany asc, 
destination_ct desc, 
destination asc, 
departure_time asc; 



