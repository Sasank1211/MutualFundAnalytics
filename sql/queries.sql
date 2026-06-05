# Top 5 funds by AUM

SELECT
fund_house,
SUM(aum_crore) total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

# Average nav by month

SELECT
strftime('%Y-%m',date) month,
AVG(nav)
FROM fact_nav
GROUP BY month;

# SIP YoY Growth

SELECT
month,
yoy_growth_pct
FROM monthly_sip_inflows;

# Transactions by state

SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

# Expence Ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

# Highest Return Funds 

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

#Highest Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC;

# Most Popular Categories

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

# Transactions Volume by City Tier

SELECT
city_tier,
SUM(amount_inr)
FROM fact_transactions
GROUP BY city_tier;

# Top Fund Managers

SELECT
fund_manager,
COUNT(*)
FROM dim_fund
GROUP BY fund_manager;


