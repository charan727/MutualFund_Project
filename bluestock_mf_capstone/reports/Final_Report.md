# Mutual Fund Analytics Project

## 1. Executive Summary

This project analyzes mutual fund performance using historical NAV, AUM, SIP inflows, category inflows, portfolio holdings, benchmark indices, and scheme performance data. The solution includes ETL automation, data cleaning, exploratory analysis, performance metric computation, interactive dashboards, and advanced analytics for fund recommendation.

## 2. Project Overview

The objective of this project is to build an end-to-end mutual fund analytics platform that enables investors and analysts to evaluate mutual fund performance using both return-based and risk-adjusted metrics.

## 3. Data Sources

* Fund Master Data
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Counts
* Scheme Performance Data
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

## 4. ETL Pipeline

The ETL pipeline performs the following activities:

* Data ingestion from multiple CSV sources
* Data validation and quality checks
* Data cleaning and preprocessing
* Standardization of column names and formats
* Processed dataset generation for analytics

## 5. Data Cleaning & Preprocessing

The preprocessing phase includes:

* Handling missing values
* Removing duplicate records
* Standardizing column formats
* Converting data types
* Preparing analytics-ready datasets

## 6. Exploratory Data Analysis (EDA)

EDA was performed to understand:

* Fund category distribution
* Return trends across schemes
* AUM concentration
* SIP inflow patterns
* Benchmark comparisons

Key observations showed variations in performance across categories and strong relationships between risk and return.

## 7. Performance Analytics

Performance analytics were calculated using industry-standard mutual fund evaluation metrics.

### Metrics Calculated

* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Annualized Volatility
* Maximum Drawdown

These metrics help evaluate fund performance from both return and risk perspectives.

### Key Observations

* Funds with higher Sharpe Ratios delivered better risk-adjusted returns.
* Alpha identified funds that outperformed benchmark expectations.
* Maximum Drawdown highlighted downside risk exposure.
* Beta measured sensitivity to market movements.

---

## 8. Power BI Dashboard

An interactive Power BI dashboard was developed to visualize fund performance and analytics.

### Dashboard Pages

#### Page 1 – Fund Overview

* Total Fund Score
* Fund Ranking Table
* Overall Fund Performance

#### Page 2 – Performance Analysis

* Alpha Comparison
* Beta Comparison
* Alpha vs Beta Analysis

#### Page 3 – Fund Insights

* Sharpe Ratio Comparison
* Maximum Drawdown Comparison
* Alpha vs Beta Visualization

#### Page 4 – Performance Overview

* Fund Score Summary
* Sharpe Ratio Summary
* Interactive Slicers and Filters

### Dashboard Features

* Interactive filtering
* Fund comparison
* Risk analysis
* Performance evaluation
* Visual insights

---

## 9. Advanced Analytics

Advanced analytics were implemented to generate investment insights and fund recommendations.

### Recommendation Engine

A recommendation score was developed using:

* Sharpe Ratio
* Alpha
* Morningstar Rating
* Expense Ratio

Funds were ranked based on a weighted scoring model.

### Category Analysis

Category-level analysis was performed to identify categories with superior long-term returns and risk-adjusted performance.

### Risk Analysis

Risk distribution analysis was conducted using risk grades and volatility metrics to classify mutual funds.

---

## 10. Key Findings

* High Sharpe Ratio funds consistently ranked among top-performing schemes.
* Expense Ratio negatively impacted overall recommendation scores.
* Certain categories outperformed peers across multiple performance metrics.
* Risk-adjusted measures provided more meaningful insights than absolute returns.

---

## 11. Recommendations

* Prioritize funds with strong Sharpe Ratios and Alpha values.
* Monitor expense ratios before investment decisions.
* Diversify investments across categories.
* Use risk-adjusted metrics rather than relying solely on historical returns.

---

## 12. Conclusion

This project successfully delivered a complete Mutual Fund Analytics Platform covering data ingestion, cleaning, performance analysis, dashboard visualization, and advanced analytics.

The solution enables data-driven fund evaluation through risk-adjusted performance metrics, interactive dashboards, and recommendation models, helping investors make informed investment decisions.
