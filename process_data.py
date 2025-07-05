import pandas as pd
import os

# Set the full path to your dataset
input_path = r"C:\Users\HP\Desktop\ci-cd-titanic\data\dataset.csv"
output_path = r"C:\Users\HP\Desktop\ci-cd-titanic\data\processed_dataset.csv"

# Load dataset
df = pd.read_csv(input_path)

# Drop duplicates
df_cleaned = df.drop_duplicates()

# Save the cleaned dataset
df_cleaned.to_csv(output_path, index=False)

# Output number of duplicates removed
print(f"✅ Removed {len(df) - len(df_cleaned)} duplicate rows.")
