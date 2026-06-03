-- ========================================================
-- BLUESTOCK MUTUAL FUND CAPSTONE PROJECT - STAR SCHEMA DESIGN
-- Deliverable: schema.sql (Database Architecture Definition)
-- ========================================================

-- 1. Dimension Table: Fund Master Data
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_name TEXT NOT NULL
);

-- 2. Dimension Table: Date Matrix Layout
CREATE TABLE IF NOT EXISTS dim_date (
    date TEXT PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
);

-- 3. Fact Table: Daily Net Asset Value (NAV) Records
CREATE TABLE IF NOT EXISTS fact_nav (
    amfi_code INTEGER,
    date TEXT,
    nav REAL NOT NULL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

-- 4. Fact Table: Investor Transactions Activity
CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amfi_code INTEGER,
    transaction_type TEXT CHECK(transaction_type IN ('SIP', 'Lumpsum', 'Redemption')),
    amount INTEGER NOT NULL,
    date TEXT,
    state TEXT,
    kyc_status TEXT CHECK(kyc_status IN ('VERIFIED', 'PENDING', 'FAILED')),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

-- 5. Fact Table: Scheme Historical Return Performance
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    returns REAL,
    expense_ratio REAL,
    expense_anomaly_flag INTEGER CHECK(expense_anomaly_flag IN (0, 1)),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- 6. Fact Table: Asset Under Management (AUM) Matrix
CREATE TABLE IF NOT EXISTS fact_aum (
    amfi_code INTEGER PRIMARY KEY,
    aum_crores REAL NOT NULL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);
