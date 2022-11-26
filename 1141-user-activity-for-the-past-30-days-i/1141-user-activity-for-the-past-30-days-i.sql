/* Write your PL/SQL query statement below */



SELECT TO_CHAR(TO_DATE(activity_date, 'YYYY-MM-DD')) AS "day", COUNT(DISTINCT user_id) AS "active_users"
FROM Activity
WHERE (activity_date > '2019-06-27' AND activity_date <= '2019-07-27')
GROUP BY activity_date;
             