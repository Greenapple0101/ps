SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, r.CREATED_DATE
from used_goods_board b
join USED_GOODS_REPLY r on r.board_id=b.board_id
where '2022-10-01'<=b.created_date and b.created_date <'2022-11-01'
order by r.created_date asc, b.title asc
