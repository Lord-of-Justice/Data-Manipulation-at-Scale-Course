SELECT a.docid, b.docid, sum(a.count*b.count) as value 
FROM Frequency a, Frequency b ON a.term = b.term
WHERE a.docid = "10080_txt_crude" 
	and b.docid = "17035_txt_earn"
GROUP BY a.docid, b.docid