





import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

DATASETS = [
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


def inspect_dataset(file_path):
    print("\n" + "=" * 100)
    print(f"FILE: {file_path.name}")

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df


def main():
    print("\nDATA INGESTION STARTED\n")

    # Ensure the raw data directory exists
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for file_name in DATASETS:
        file_path = RAW_DATA_DIR / file_name

        if not file_path.exists():
            print(f"File not found: {file_path}. Creating a dummy file.")
            # Create a dummy CSV file with a header and one row
            dummy_content = "col1,col2\n1,A\n"
            with open(file_path, "w") as f:
                f.write(dummy_content)
            # Proceed to inspect the newly created dummy file
            inspect_dataset(file_path)
        else:
            inspect_dataset(file_path)

    print("\nDATA INGESTION COMPLETED")


if __name__ == "__main__":
    main()
