CREATE VIEW IF NOT EXISTS tableForPhrase AS
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT a.docid, b.docid, sum(a.count*b.count) as similarity 
FROM tableForPhrase a INNER JOIN tableForPhrase b ON a.term = b.term
WHERE a.docid = "q" and b.docid != "q"
GROUP BY a.docid, b.docid
ORDER BY similarity DESC