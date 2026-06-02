import os
import requests
import pandas as pd

os.makedirs('data/raw', exist_ok=True)

url_hdfc = "https://mfapi.in"
r = requests.get(url_hdfc)

import pandas as pd
for code in ["125097", "120503", "118632", "119092", "120841"]:
    df = pd.read_json(f"https://mfapi.in{code}")
    df.to_csv(f"data/raw/{code}.csv")
    print(f"Done {code}")