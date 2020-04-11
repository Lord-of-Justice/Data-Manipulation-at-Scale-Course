SELECT count(*) FROM (
	SELECT DISTINCT docid FROM Frequency
	WHERE term = "law" OR term = "legal"
)