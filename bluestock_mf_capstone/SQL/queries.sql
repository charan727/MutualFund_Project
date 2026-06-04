-- Query 1: Top 5 Funds by AUM
SELECT f.fund_name, a.aum_crores FROM fact_aum a JOIN dim_fund f ON a.amfi_code = f.amfi_code ORDER BY a.aum_crores DESC LIMIT 5;

-- Query 2: Average NAV Per Month
SELECT strftime('%m', date) as Month, AVG(nav) as Avg_NAV FROM fact_nav GROUP BY Month;

-- Query 3: SIP Year-over-Year Volume Metrics
SELECT strftime('%Y', date) as Year, COUNT(*) as Total_SIPs, SUM(amount) as Total_Volume FROM fact_transactions WHERE transaction_type = 'SIP' GROUP BY Year;

-- Query 4: Total Transaction Volumes by State
SELECT state, COUNT(*) as Transaction_Count, SUM(amount) as Total_Amount FROM fact_transactions GROUP BY state ORDER BY Total_Amount DESC;

-- Query 5: High Efficiency Funds with Expense Ratio < 1%
SELECT fund_name, expense_ratio FROM fact_performance WHERE expense_ratio < 1.0;

-- Query 6: KYC Status Distribution Report
SELECT kyc_status, COUNT(*) as Total_Investors FROM fact_transactions GROUP BY kyc_status;

-- Query 7: Anomalous Schemes Flagged Check
SELECT fund_name, expense_ratio FROM fact_performance WHERE expense_anomaly_flag = 1;

-- Query 8: Total Redemptions Capital Outflow
SELECT SUM(amount) as Total_Outflow FROM fact_transactions WHERE transaction_type = 'Redemption';

-- Query 9: Fund Count in Master Layout
SELECT COUNT(DISTINCT amfi_code) as Total_Active_Funds FROM dim_fund;

-- Query 10: Maximum Portfolio Returns Mapping
SELECT f.fund_name, p.returns FROM fact_performance p JOIN dim_fund f ON p.amfi_code = f.amfi_code ORDER BY p.returns DESC LIMIT 1;
