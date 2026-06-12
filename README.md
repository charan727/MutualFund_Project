# Mutual Fund Analytics Capstone Project

## Project Overview

This project builds an end-to-end Mutual Fund Analytics platform using Python, SQLite, Power BI, and GitHub. The solution performs data ingestion, cleaning, exploratory data analysis, performance analysis, advanced analytics, and dashboard visualization for mutual fund schemes.

---

## Business Objective

The objective of this project is to help investors and analysts evaluate mutual fund performance using return-based and risk-adjusted metrics and provide insights through interactive dashboards.

---

## Dataset Description

The project uses the following datasets:

- Fund Master Data
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Counts
- Scheme Performance Data
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices

---

## Project Architecture

Raw CSV Files
→ Data Ingestion
→ Data Cleaning
→ SQLite Database
→ EDA Analysis
→ Performance Analysis
→ Advanced Analytics
→ Power BI Dashboard
→ Final Report & Presentation

---

## ETL Pipeline

### Data Ingestion
- Load source CSV files
- Validate file structure
- Store data in SQLite

### Data Cleaning
- Handle missing values
- Standardize column names
- Convert data types
- Remove duplicates

---

## Exploratory Data Analysis

The following analyses were performed:

- Industry AUM trend analysis
- SIP inflow trend analysis
- Category-wise inflow analysis
- Fund house comparison
- Scheme performance analysis
- Investor transaction analysis

---

## Performance Analysis

Performance metrics calculated:

- Annualized Return
- Sharpe Ratio
- Alpha
- Maximum Drawdown
- Historical VaR
- Historical CVaR

---

## Advanced Analytics

### Fund Recommendation Engine
Ranked schemes based on:
- Sharpe Ratio
- Alpha
- Maximum Drawdown

### Rolling Sharpe Analysis
30-day rolling Sharpe Ratio trend analysis.

### Cohort Analysis
Investor transaction cohort behavior analysis.

### SIP Continuity Analysis
Identified SIP continuity and investment consistency patterns.

---

## Dashboard Overview

Power BI dashboard contains:

### Industry Overview
- Total AUM
- SIP Inflows
- Folios
- Scheme Count

### Fund Insights
- Category Comparison
- Fund House Comparison
- Investor Activity

### Performance Overview
- Sharpe Ratio
- Alpha
- Drawdown
- Fund Recommendation Scores

---

## Project Structure

```text
MutualFund_Project/
│
├── data/
├── notebooks/
├── scripts/
├── reports/
├── dashboard/
├── README.md
├── requirements.txt
└── run_pipeline.py