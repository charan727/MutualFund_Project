import os
import requests
import pandas as pd
import json

# Create data directory if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

print("=" * 80)
print("LIVE NAV FETCHING - FETCHING DATA FROM MFAPI.IN")
print("=" * 80)

# Dictionary of key mutual fund schemes with their AMFI codes
schemes = {
    "125497": "HDFC Top 100 Direct",
    "119551": "SBI Bluechip Direct",
    "120503": "ICICI Bluechip Direct",
    "118632": "Nippon Large Cap Direct",
    "119092": "Axis Bluechip Direct",
    "120841": "Kotak Bluechip Direct"
}

base_url = "https://api.mfapi.in/mf"

for code, scheme_name in schemes.items():
    try:
        url = f"{base_url}/{code}"
        print(f"\nFetching: {scheme_name} (Code: {code})")
        print(f"URL: {url}")
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Create DataFrame from the data
        if isinstance(data, dict) and 'data' in data:
            df = pd.DataFrame(data['data'])
        else:
            df = pd.DataFrame(data)
        
        # Save to CSV
        csv_file = f"data/raw/{code}_{scheme_name.replace(' ', '_')}.csv"
        df.to_csv(csv_file, index=False)
        print(f"✓ Saved: {csv_file}")
        print(f"  Records: {len(df)}")
        print(f"  Columns: {list(df.columns)}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching {scheme_name} (Code: {code}): {str(e)}")
    except Exception as e:
        print(f"✗ Error processing {scheme_name} (Code: {code}): {str(e)}")

print("\n" + "=" * 80)
print("LIVE NAV FETCHING COMPLETE")
print("=" * 80)