import requests
import pandas as pd

SCHEME_CODE = 125497

url = f"https://api.mfapi.in/mf/{SCHEME_CODE}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    print("\nSample NAV Data:")
    print(nav_df.head())

    nav_df.to_csv(
        "Data/raw/hdfc_top_100_direct_nav.csv",
        index=False
    )

    print("\nCSV saved successfully!")

else:
    print("Failed to fetch NAV data")
