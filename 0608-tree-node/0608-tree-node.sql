/* Write your PL/SQL query statement below */
select id,
CASE
   when p_id is null then 'Root'
   when id in (select p_id from Tree) then 'Inner'
else 'Leaf'
end "type"
from Tree ;


