# RETAIL SALES ANALYSIS USING PYTHON
# Intermediate Level Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATASET

file_path = r"C:\Users\harzs\Downloads\Beginner analysis.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("\nDATASET OVERVIEW")
print(df.head())
print("\nDataset Shape:", df.shape)

# 2. DATA CLEANING

print("\nMISSING VALUES")
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna(subset=["Sales", "Profit", "Order Date"])

df["Order Date"]=pd.to_datetime(df["Order Date"],format="%m%d%Y",errors="coerce")
df = df.dropna(subset=["Order Date"])

print("\nCleaned Dataset Shape:", df.shape)

# 3. OVERALL SALES PERFORMANCE

print("\nOVERALL SALES PERFORMANCE")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Quantity:", df["Quantity"].sum())

# 4. REGION-WISE ANALYSIS

region = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nREGION-WISE ANALYSIS")
print(region)

# 5. CATEGORY ANALYSIS

category = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nCATEGORY ANALYSIS")
print(category)

# 6. SUB-CATEGORY ANALYSIS

subcategory = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nSUB-CATEGORY ANALYSIS")
print(subcategory)

# 7. CUSTOMER SEGMENT ANALYSIS

segment = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nCUSTOMER SEGMENT ANALYSIS")
print(segment)

# 8. DISCOUNT ANALYSIS

discount = df.groupby("Discount").agg(
    Average_Sales=("Sales", "mean"),
    Average_Profit=("Profit", "mean")
)

print("\nDISCOUNT ANALYSIS")
print(discount)

# 9. SHIPPING MODE ANALYSIS

shipping = df.groupby("Ship Mode").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
)

print("\nSHIPPING MODE ANALYSIS")
print(shipping)

# 10. MONTHLY SALES TREND

df["Year-Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Year-Month")["Sales"].sum()

print("\nMONTHLY SALES TREND")
print(monthly_sales)

# 11. DATA VISUALIZATION

sns.set_theme(style="whitegrid")

region["Total_Sales"].plot(
    kind="bar", title="Region-wise Sales"
)
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

category["Total_Profit"].plot(
    kind="bar", title="Category-wise Profit"
)
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

subcategory["Total_Profit"].sort_values().plot(
    kind="barh", title="Sub-category Profit"
)
plt.tight_layout()
plt.show()

segment["Total_Sales"].plot(
    kind="pie", autopct="%1.1f%%",
    title="Sales by Customer Segment"
)
plt.ylabel("")
plt.tight_layout()
plt.show()

monthly_sales.index = monthly_sales.index.astype(str)
monthly_sales.plot(
    kind="line", marker="o",
    title="Monthly Sales Trend"
)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Discount", y="Profit")
plt.title("Discount vs Profit")
plt.tight_layout()
plt.show()

shipping["Total_Sales"].plot(
    kind="bar", title="Sales by Shipping Mode"
)
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# 12. BUSINESS INSIGHTS

print("\nBUSINESS INSIGHTS")

print("Highest Sales Region:",
      region["Total_Sales"].idxmax())

print("Top Sales Category:",
      category["Total_Sales"].idxmax())

print("Top Customer Segment:",
      segment["Total_Sales"].idxmax())

print("Most Profitable Sub-Category:",
      subcategory["Total_Profit"].idxmax())

print("\nRETAIL SALES ANALYSIS COMPLETED!")
