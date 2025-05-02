--products that user has viewed and 
--puchased 
with cte as (select 
user_id, 
product_id 
from 
product_views v 
inner join 
purchases p 
on v.product_id = p.product_id)   

select product_id from product_views 
where product_id not in (
    select distinct product_id from cte
);




