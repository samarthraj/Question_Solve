--eco_products
product_id
product_name
category
is_sustainable (boolean: TRUE if sustainable, FALSE if not)

--procurement_data
product_id
purchase_date
purchase_quantity
price_per_unit

with cte as (select 
p.product_id, 
e.product_name, 
sum(p.purchase_quantity * p.price_per_unit) as total_sum 
from procurement_data p
inner join eco_products e 
on p.product_id = e.product_id 
where e.is_sustainable = TRUE 
group by p.product_id, 
e.product_name), 

cte2 as (select 
avg(total_sum) as avg_total_cost 
from cte)

select 
product_id,
product_name,
total_sum 
from cte where 
cte.total_sum > (select avg_total_cost from cte2)


