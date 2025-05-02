--percentage of late deliveries 
--Top 3 warehouses 
--(no of deliveries where actual > expecd/ total no of deliveries) group by warehouse_id 

with cte as (select 
warehouse_id, 
count(*) as total_deliveries 
from shipments
group by warehouse_id), 

cte2 as (select 
warehouse_id, 
count(*) as total_actual_deliveries 
from shipments
where actual_delivery_date > expected_delivery_date
group by warehouse_id), 

rate_cte as (select cte.warehouse_id, 
cte2.total_actual_deliveries, 
cte.total_deliveries,
round((cte2.total_actual_deliveries / cte.total_deliveries)*100,2) as delivery_rate 
from cte inner join cte2 on 
cte.warehouse_id = cte2.warehouse_id), 

select r.warehouse_id, 
w.warehouse_name,
r.total_actual_deliveries, 
r.total_deliveries, 
r.delivery_rate 
from rate_cte r inner join warehouses w 
on w.warehouse_id = r.warehouse_id 
order by r.delivery_rate desc 
limit 3; 
 





