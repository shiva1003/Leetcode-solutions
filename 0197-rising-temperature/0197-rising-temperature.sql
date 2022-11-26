
select w1.id as "id" from weather w1 join weather w2 
on (w1.recordDate - w2.recordDate)=1
and w1.temperature > w2.temperature ;



/* MYSQL
SELECT p.Id
	FROM weather p, weather q
	WHERE TO_DAYS(p.RecordDate) - TO_DAYS(q.RecordDate) = 1
	AND p.Temperature > q.Temperature;
    
SELECT p.Id
	FROM weather p, weather q
	WHERE DATEDIFF(p.RecordDate, q.RecordDate)=1
	AND p.Temperature > q.Temperature;
*/



