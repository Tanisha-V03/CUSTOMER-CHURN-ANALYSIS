SELECT * FROM customer_churn;

-- 1.) TOTAL CUSTOMERS
SELECT
	COUNT(*) 
FROM 
	customer_churn;

-- 2.) TOTAL CHURN CUSTOMERS
SELECT
	COUNT(*) 
FROM 
	customer_churn
WHERE "Churn" = 'Yes';

-- 3.) CHURN RATE
SELECT
	ROUND(
		SUM(CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END)*100/COUNT(*), 2) AS CHURN_RATE
FROM 
	customer_churn;

-- 4.) AVERAGE MONTHLY CHARGES
SELECT
	AVG("Monthly_Charges") 
FROM 
	customer_churn;

-- 5.) AVERAGE TENURE
SELECT
	AVG("Tenure_Months") 
FROM 
	customer_churn;

-- 6.) CHURN BY CONTRACT TYPE
SELECT
	"Contract_Type", 
	COUNT(*) AS CUSTOMERS
FROM 
	customer_churn
GROUP BY 
	1;
	
-- 7.) CHURN BY INTERNET SERVICES
SELECT
	"Internet_Service", 
	COUNT(*) AS CUSTOMERS
FROM 
	customer_churn
GROUP BY 
	1;

-- 8.) CHURN BY SATE
SELECT
	"State", 
	COUNT(*) AS CUSTOMERS
FROM 
	customer_churn
WHERE
	"Churn" = 'Yes'
GROUP BY 
	1
ORDER BY 
	2;

-- 9.) PAYMENT METHOD WISE CUSTOMERS
SELECT
	"Payment_Method", 
	COUNT(*) AS CUSTOMERS
FROM 
	customer_churn
GROUP BY 
	1;

-- 10.) SUBSCRIPTION METHOD WISE CUSTOMERS
SELECT
	"Subscription_Type", 
	COUNT(*) AS CUSTOMERS
FROM 
	customer_churn
GROUP BY 
	1;

-- 11) HIGHEST REVENUE STATES
SELECT
	"State", 
	SUM("Total_Charges") AS STATE_CHARGES
FROM 
	customer_churn
GROUP BY 
	1
ORDER BY 
	2 DESC;

-- 12) AVERAGE CHARGES BY CONTRACT
SELECT
	"Contract_Type", 
	AVG("Monthly_Charges")
FROM 
	customer_churn
GROUP BY 
	1;

-- 13) SENIOR CITIZEN CHURN
SELECT
	"Senior_Citizen", 
	COUNT(*)
FROM 
	customer_churn
WHERE "Churn" = 'Yes'
GROUP BY 
	1;

-- 14) TOP 10 HIGH VALUE CUSTOMERS
SELECT
	"Customer_Name", 
	"Customer_Value"
FROM 
	customer_churn
ORDER BY 
	2 DESC
LIMIT
	10;

-- 15.) CUSTOMER WITHOUT TECH SUPPORT
SELECT
	*
FROM
	customer_churn
WHERE
	"Tech_Support" = 'No';











