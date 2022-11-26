/* Write your PL/SQL query statement below */
select * from patients where (conditions like 'DIAB1%' OR conditions like '% DIAB1%') ;