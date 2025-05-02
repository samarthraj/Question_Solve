with user_views_and_purchased_table
as (select 
p.user_id, 
p.product_id, 
v.view_date, 
p.purchase_date 
from views v 
inner join purchases p 
on v.user_id = p.user_id 
and v.product_id = p.product_id
and p.purchase_date > v.view_date),   

v_p_ct_cte as (select 
count(distinct user_id) as user_ct, 
product_id 
from user_views_and_purchased_table 
group by product_id), 

v_cte as (select 
count(distinct user_id) as viewer_count, 
product_id from 
views group by product_id 
having count(distinct user_id) >= 10)

select 
t1.product_id, 
round((t1.user_ct*100/t2.viewer_count),2) as conversion_rate from 
v_p_ct_cte t1 inner join v_cte t2 
on t1.product_id = t2.product_id 
