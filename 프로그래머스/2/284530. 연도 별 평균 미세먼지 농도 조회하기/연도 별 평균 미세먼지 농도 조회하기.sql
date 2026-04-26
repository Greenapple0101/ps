SELECT YEAR(ym) AS year, 
       ROUND(AVG(pm_val1),2) AS 'pm10', 
       ROUND(AVG(pm_val2),2) AS 'pm2.5'
FROM air_pollution
where location2 LIKE "%수원%"
group by year(ym)
ORDER BY year ASC;