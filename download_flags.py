import os
import requests
import pandas as pd
import pycountry

# --- Step 1: Load your COVID dataset ---
csv_path = "owid-covid-data.csv"  # CSV is in project root
df = pd.read_csv(csv_path)

# --- Step 2: Get unique ISO alpha-3 codes from your dataset ---
iso3_codes = df['iso_code'].dropna().unique()

# --- Step 3: Create folder for flags ---
os.makedirs("assets/flags", exist_ok=True)

# --- Step 4: Function to convert ISO3 -> ISO2 ---
def iso3_to_iso2(code):
    try:
        country = pycountry.countries.get(alpha_3=code)
        return country.alpha_2
    except:
        return None

# --- Step 5: Download each flag ---
for iso3 in iso3_codes:
    iso2 = iso3_to_iso2(iso3)
    if iso2 is None:
        print(f"Cannot map {iso3}, skipping")
        continue
    url = f"https://flagcdn.com/w80/{iso2.lower()}.png"  # small 80px width
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"assets/flags/{iso3}.png", "wb") as f:  # save with alpha-3 code
            f.write(response.content)
        print(f"{iso3} flag downloaded ✅")
    else:
        print(f"Failed to download {iso3}")
