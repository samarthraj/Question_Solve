with 
users_added_to_cart_and_purchased_cte
as (select 
p.user_id, 
p.product_id 
from purchases p 
inner join cart_additions c 
on p.user_id = c.user_id 
and p.product_id = c.product_id ) 

select 
c.user_id, 
c.product_id 
from cart_additions c 
left join users_added_to_cart_and_purchased_cte u 
on c.user_id = u.user_id 
and c.product_id = u.product_id 
where u.user_id is Null
