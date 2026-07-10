import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
try:
    df = pd.read_csv("data/sales_data.csv")
    print("Dataset Loaded Successfully")
except FileNotFoundError:
    print("Dataset Not Found")
    exit()

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
df.info()

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()
print("\nMissing values removed.")

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)
print("Duplicate rows removed.")

# Display Column Names
print("\nColumns:")
print(df.columns)

# Basic Analysis
print("\n========== SALES ANALYSIS ==========")
print("Total Sales:", df["Total_Sales"].sum())
print("Average Sales:", df["Total_Sales"].mean())
print("Highest Sale:", df["Total_Sales"].max())
print("Lowest Sale:", df["Total_Sales"].min())
print("Total Quantity Sold:", df["Quantity"].sum())