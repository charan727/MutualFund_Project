import pandas as pd
import os

# Path to raw data folder
data_path = "data/raw"

# Example list of CSV files
files = [
    "fund_master.csv",
    "nav_history.csv",
    "transactions.csv"
]

for f in files:
    file_path = os.path.join(data_path, f)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"\nFile: {f}")
        print("Shape:", df.shape)
        print("Dtypes:\n", df.dtypes)
        print("Head:\n", df.head())
    else:
        print(f"{f} not found in raw folder")