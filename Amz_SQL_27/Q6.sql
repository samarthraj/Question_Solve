with cte1 as (select 
project_id,
count(*) as total_facilities, 
sum(
    case 
    when actual_completion_date <= expected_completion_date then 1
    else 0 
    end  
) as on_time_facilities, 
sum(
    case 
    when actual_completion_date > expected_completion_date then 1
    else 0 
    end  
) as delayed_facilities 
from sustainability_projects 
group by project_id) 

select 
project_id, 
round(on_time_facilities*100/total_facilities,2) as on_time_percentage, 
round(delayed_facilities*100/total_facilities,2) as delayed_percentage 
from cte1




