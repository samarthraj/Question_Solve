WITH all_user_logins_per_month AS (
  SELECT 
    user_id, 
    DATE_FORMAT(login_date, '%Y-%m') AS month_date 
  FROM user_logins
), 
all_users AS (
  SELECT DISTINCT user_id FROM user_logins
), 
all_months AS (
  SELECT DISTINCT DATE_FORMAT(login_date, '%Y-%m') AS month_date 
  FROM user_logins
), 
user_month_matrix AS (
  SELECT 
    u.user_id, 
    m.month_date
  FROM all_users u 
  CROSS JOIN all_months m
), 
user_month_logins AS (
  SELECT DISTINCT 
    user_id, 
    month_date 
  FROM all_user_logins_per_month
), 
inactive_flags AS (
  SELECT 
    umm.month_date, 
    umm.user_id, 
    CASE 
      WHEN uml.user_id IS NULL THEN 1 
      ELSE 0 
    END AS is_inactive
  FROM user_month_matrix umm
  LEFT JOIN user_month_logins uml 
    ON umm.user_id = uml.user_id AND umm.month_date = uml.month_date
), 
inactive_users_per_month AS (
  SELECT 
    month_date, 
    COUNT(*) AS inactive_users
  FROM inactive_flags
  WHERE is_inactive = 1
  GROUP BY month_date
), 
active_users_per_month AS (
  SELECT 
    month_date, 
    COUNT(DISTINCT user_id) AS active_users
  FROM all_user_logins_per_month
  GROUP BY month_date
)

SELECT 
  a.month_date,
  a.active_users,
  COALESCE(i.inactive_users, 0) AS inactive_users
FROM active_users_per_month a
LEFT JOIN inactive_users_per_month i 
  ON a.month_date = i.month_date
ORDER BY a.month_date;
