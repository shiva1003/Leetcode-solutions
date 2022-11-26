

select *
from products unpivot(
                      price for store in (store1 as 'store1',store2 as 'store2',store3 as 'store3')
    )
    
