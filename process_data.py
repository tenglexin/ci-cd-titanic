import pandas as pd
import os

# Paths
input_path = "data/dataset.csv"
output_path = "data/processed_dataset.csv"

# Make sure the output folder exists
os.makedirs("data", exist_ok=True)

# Load and clean dataset
df = pd.read_csv(input_path)
df_clean = df.drop_duplicates()

# Save cleaned dataset
df_clean.to_csv(output_path, index=False)

# Print result (uses df_clean, not df_cleaned)
print(f"✅ Removed {len(df) - len(df_clean)} duplicate rows.")
