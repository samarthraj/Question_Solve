--average quantity sold per month 
--3 consecutive months 
with cte as (select p.category, 
p.product_name,
date_format(s.sale_date, '%Y-%m') as sale_month, 
avg(s.quantity_sold) as avg_sold
from sales s
inner join 
products p on 
s.product_id = p.product_id
where s.sale_date >= date_sub(current_date, interval 3 month)
group by p.category, 
s.sale_month),  

cte2 as (select 
category, 
product_name,
sale_month, 
avg_sold, 
lag(avg_sold, 1) over (partition by category order by sale_month) as lg1, 
lag(avg_sold, 2) over (partition by category order by sale_month) as lg2 
from cte)  

select category,  
product_name, 
avg_sold 
from cte2
where cte2.lg1 > cte2.avg_sold  and cte2.lg2 > cte2.lg1
  









