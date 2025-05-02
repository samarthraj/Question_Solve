product_views(user_id, product_id)
purchases(user_id, product_id)
products(product_id, category) 

with cte1 as (select 
v.user_id, v.product_id, pro.category 
from product_views v 
inner join products pro 
on 
v.product_id = pro.product_id), 

only_viewer_ct as (select 
count(distinct user_id) as viewers, 
category 
from cte1 
group by category
having count(distinct user_id) >= 100), 

purchase_after_view as (select 
count(distinct p.user_id) as purchasers, 
v.category
from purchases p 
inner join 
cte1 v 
on p.user_id = v.user_id 
and p.product_id = v.product_id
group by v.category) 

select 
v.category, 
v.viewers, 
p.purchasers, 
round((p.purchasers*100)/v.viewers, 2) as 
conversion_rate 
from only_viewer_ct v 
inner join purchase_after_view p 
on v.category = p.category

