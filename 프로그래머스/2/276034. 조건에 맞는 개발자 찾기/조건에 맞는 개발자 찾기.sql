select distinct d.id,d.email,d.first_name,d.last_name
from skillcodes s
join developers d on (d.skill_code & s.code) = s.code
WHERE s.name IN ('C#', 'Python')
order by id