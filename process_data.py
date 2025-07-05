import pandas as pd
import os

# Correct relative paths for Linux/Windows compatibility
input_path = "data/dataset.csv"
output_path = "data/processed_dataset.csv"

# Make sure the data folder exists
os.makedirs("data", exist_ok=True)

# Read and deduplicate
df = pd.read_csv(input_path)
df_clean = df.drop_duplicates()
df_clean.to_csv(output_path, index=False)

# Output number of duplicates removed
print(f"✅ Removed {len(df) - len(df_cleaned)} duplicate rows.")
