import pandas as pd
import os

data_path = "Data/raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print("\n" + "="*80)
    print(f"Dataset: {file}")
    print("="*80)

    df = pd.read_csv(os.path.join(data_path, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

# #####################################################Explore Fund Master#################################################
print("\nColumns in Fund Master:")
print(fund_master.columns.tolist())

fund_master = pd.read_csv(
    os.path.join(data_path, "01_fund_master.csv")
)

nav_history = pd.read_csv(
    os.path.join(data_path, "02_nav_history.csv")
)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["subcategory"].unique())

print("\nRisk Grades:")
print(fund_master["risk_grade"].unique())


missing_codes = set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])

print("Missing Codes:", missing_codes)

print("Count:", len(missing_codes))

# ############################################# Validate AMFI Codes##################################################

fund_master_codes = set(fund_master["amfi_code"])
nav_history_codes = set(nav_history["amfi_code"])

missing_codes = fund_master_codes - nav_history_codes

print("\nAMFI Code Validation")
print("-" * 50)

print(f"Total AMFI Codes in Fund Master: {len(fund_master_codes)}")
print(f"Total AMFI Codes in NAV History: {len(nav_history_codes)}")
print(f"Missing Codes: {len(missing_codes)}")

if len(missing_codes) == 0:
    print("Validation Passed: All AMFI codes in fund_master exist in nav_history.")
else:
    print("Validation Failed. Missing Codes:")
    print(missing_codes)
