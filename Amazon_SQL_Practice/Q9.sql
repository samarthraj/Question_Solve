with cte as (select 
    category, 
    avg(price) as avg_category_price
from products
group by category) 

select 
    product_id, 
    category, 
    price 
    from products 
    where category in (select category from cte) 
