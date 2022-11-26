/* Write your PL/SQL query statement below */
select employee_id from (select employee_id from employees where employee_id not in (select employee_id from salaries) 
union 
(select employee_id from salaries where employee_id not in (select employee_id from employees))) order by employee_id ;