select *, 
row_number() over 
(partition by customer_id
order by order_date) as rnk 
from orders