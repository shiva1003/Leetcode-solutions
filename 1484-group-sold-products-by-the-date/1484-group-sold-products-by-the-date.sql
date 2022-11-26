/* Write your PL/SQL query statement below */

select to_char(a.sell_date, 'yyyy-mm-dd') sell_date
    , count(a.product) num_sold
    , listagg(a.product, ',') within group(order by a.product) products
from (select distinct * from activities) a
group by a.sell_date
order by a.sell_date