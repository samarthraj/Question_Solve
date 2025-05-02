
with view_ct_cte as (select 
count(distinct user_id) as view_ct, 
product_id 
from product_views 
group by product_id having 
count(distinct user_id) >= 10)

users_purchased_after_view as (select 
count(distinct p.user_id) as purchse_ct_af_view, 
p.product_id 
from purchases p 
inner join product_views v 
on p.user_id = v.user_id 
and p.product_id = v.product_id
group by p.product_id), 

fin_cte as (select 
v.view_ct, 
p.purchse_ct_af_view, 
v.product_id  
from view_ct_cte v 
inner join users_purchased_after_view p on 
v.product_id = p.product_id) 

select product_id, 
round((purchse_ct_af_view/view_ct)*100,2) 
as conversion_rate from fin_cte


