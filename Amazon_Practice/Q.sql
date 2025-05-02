--past 6 months
with cte as (select c.customer_id, 
c.region, 
o.order_date, 
sum(o.amount) as total_spent
from customers c inner join orders o on 
c.customer_id = o.customer_id 
where  o.order_date between current_date - interval '6 months' and current_date 
group by c.customer_id, c.region 
) 

select region, 
customer_id, 
total_spent, 
dense_rank() over (partition by region order by total_spent desc) as rnk 
from cte 
where rnk <= 5

