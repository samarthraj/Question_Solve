--first 30 days 
--sales volumne and revenue 

select p.product_id, 
p.product_name, 
p.launch_date, 
sum(o.quantity) as total_quantity_sold, 
sum(o.price_per_unit*o.quantity) as total_revenue 
from 
products p 
inner join order o 
on p.product_id = o.product_id 
where 
o.order_date between p.launch_date and 
date_add(p.launch_date, interval 30 day) 
group by 
p.product_id, p.product_name, p.launch_date
order by total_revenue desc