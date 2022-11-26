/* Write your PL/SQL query statement below */
select max(salary) as SecondHighestSalary from employee 
where salary < (select max(salary) from employee) ;
