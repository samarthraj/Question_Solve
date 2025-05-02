--July 11, 12 2023 
--compared to a normal week 
--boosted user_activity 

--unique users who purchased on prime day 
with cte as (
select 
count(distinct user_id) as user_unique_ct,  
product_id 
from purchases 
where purchase_date between'2023-07-11' and 
'2023-07-12' 
group by product_id), 

cte2 as (select 
count(distinct user_id) as user_id_before_ct, 
product_id 
from views 
where view_date < '2023-07-11' 
group by product_id 
having count(distinct user_id) >= 10) 

select 
v.product_id, 
(p.user_unique_ct * 1.0 / v.user_id_before_ct) 
as conversion_rate 
from cte p inner join cte2 v on 
v.product_id = p.product_id; 


