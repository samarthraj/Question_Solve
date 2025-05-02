--total purchase amount 
with cte as (select customer_id, 
sum(amount) as total_amount, 
count(order_id) as order_ct,
region 
from orders 
where order_date between current_date - interval 6 month 
and current_date
group by customer_id, region
having count(order_id) >= 2), 

cte2 as (select 
cte.customer_id, 
c.customer_name,
cte.region, 
cte.total_amount, 
dense_rank() over (partition by cte.region 
order by cte.total_amount desc) as rnk 
from cte inner join customers c on 
cte.customer_id = c.customer_id), 

region_total as (select region, 
sum(total_amount) as region_total_amt
from orders 
where order_date between current_date - interval 6 month 
and current_date
group by region), 

fin_cte as (select customer_id, 
customer_name, 
region, 
total_amount, 
rnk from cte2 where rnk <= 5) 

select 
f.customer_id, 
f.customer_name, 
f.region, 
f.total_amount, 
(f.total_amount / r.region_total_amt)*100 as perct_contribution 
from fin_cte f inner join region_total r
on fin_cte.region = region_total.region


