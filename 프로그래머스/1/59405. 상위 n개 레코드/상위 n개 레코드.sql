SELECT NAME
from ANIMAL_INS
where datetime = (select min(datetime) from animal_ins);