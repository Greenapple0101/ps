SELECT book_id, published_date
from book
where category='인문'
and published_date between '2021-01-01' and '2021-12-31'
order by published_date asc