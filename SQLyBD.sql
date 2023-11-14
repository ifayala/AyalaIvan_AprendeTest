--2.1
SELECT *
	FROM Ventas
	WHERE Amount > 1000;

--2.3
SELECT Customer_id,Date,Amount,SUM(Amount) OVER (PARTITION BY Customer_id ORDER BY Date) ASTotal_Amt,Amount / SUM(Amount) OVER (PARTITION BY Customer_id) * 100 AS Daily_Contribution
FROM ventas
ORDER BY Customer_id,Date;

--2.4
DELETE FROM Product
	WHERE id NOT IN (
						SELECT id
						FROM (
							SELECT id,
							ROW_NUMBER() OVER (PARTITION BY product_code) AS rn
							FROM Product) p
						WHERE rn = 1
					);
