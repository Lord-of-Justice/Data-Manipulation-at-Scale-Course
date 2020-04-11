SELECT count(docid) FROM
	(SELECT DISTINCT docid FROM Frequency
	WHERE term = "transactions"
	INTERSECT
	SELECT DISTINCT docid FROM Frequency
	WHERE term = "world")