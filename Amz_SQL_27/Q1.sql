with cte as (select 
aviacompany, 
count(*) as company_count 
from flights 
group by 
aviacompany), 

cte2 as (select 
aviacompany, 
destination,
count(destination) as total_flights, 
from flights 
group by 
aviacompany, 
destination) 

select id, destination, departure_time 
from flights f 
inner join cte1 on f.aviacompany = cte.aviacompany 
inner join cte2 on f.aviacompany = cte2.aviacompany 
and f.destination = cte2.destination 
order by 
company_count desc, 
aviacompany asc, 
total_flights desc, 
destination asc, 
departure_time asc





