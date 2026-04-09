import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Display basic info
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Standardize text columns (example)
if 'type' in df.columns:
    df['type'] = df['type'].str.lower().str.strip()

if 'country' in df.columns:
    df['country'] = df['country'].str.title().str.strip()

# Convert date column if exists
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Check data types
print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("cleaned_netflix_dataset.csv", index=False)

print("\nData cleaning completed successfully!")