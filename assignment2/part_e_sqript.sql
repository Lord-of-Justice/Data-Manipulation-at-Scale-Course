SELECT docid, count(DISTINCT term) as c
FROM Frequency
GROUP BY docid
HAVING c > 300