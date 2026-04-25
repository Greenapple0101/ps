-- 코드를 작성해주세요
select Id, ifnull(LENGTH,10) as length
from fish_info
order by length desc, id asc
limit 10