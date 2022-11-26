/* Write your PL/SQL query statement below */
select v.customer_id,
count(*) as count_no_trans from visits v
left outer join
transactions t
on v.visit_id=t.visit_id    /*for giving reference*/
where t.transaction_id is null
group by v.customer_id;
