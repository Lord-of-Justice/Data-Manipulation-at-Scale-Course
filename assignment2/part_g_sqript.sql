SELECT a.row_num, b.col_num, sum(a.value*b.value) as value 
FROM a INNER JOIN b
ON a.col_num = b.row_num
WHERE a.row_num = 2 and b.col_num = 3
GROUP BY a.row_num, b.col_num