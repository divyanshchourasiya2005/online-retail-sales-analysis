
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# -------------------------
# Create images folder
# -------------------------
os.makedirs("images", exist_ok=True)

# -------------------------
# Load Dataset
# -------------------------
file_path = "Online Retail.xlsx"
df = pd.read_excel(file_path)

print("="*50)
print("ONLINE RETAIL SALES ANALYSIS")
print("="*50)

print("\nOriginal Shape:", df.shape)

# -------------------------
# Data Cleaning
# -------------------------
df.drop_duplicates(inplace=True)
df.dropna(subset=["CustomerID"], inplace=True)

df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df["Hour"] = df["InvoiceDate"].dt.hour
df["Weekday"] = df["InvoiceDate"].dt.day_name()

print("Cleaned Shape:", df.shape)

# -------------------------
# Insights
# -------------------------

print("\nTOP 10 PRODUCTS")
print(df.groupby("Description")["Revenue"].sum().nlargest(10))

print("\nTOP 10 COUNTRIES")
print(df.groupby("Country")["Revenue"].sum().nlargest(10))

print("\nMONTHLY REVENUE")
print(df.groupby("Month")["Revenue"].sum())

print("\nTOP CUSTOMERS")
print(df.groupby("CustomerID")["Revenue"].sum().nlargest(10))

# -------------------------
# Chart 1 Monthly Revenue
# -------------------------
monthly = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(10,5))
monthly.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("images/monthly_revenue.png")
plt.close()

# -------------------------
# Chart 2 Top Products
# -------------------------
top_products = df.groupby("Description")["Revenue"].sum().nlargest(10)

plt.figure(figsize=(10,5))
top_products.sort_values().plot(kind="barh")
plt.title("Top Selling Products")
plt.tight_layout()
plt.savefig("images/top_products.png")
plt.close()

# -------------------------
# Chart 3 Countries
# -------------------------
top_countries = df.groupby("Country")["Revenue"].sum().nlargest(10)

plt.figure(figsize=(10,5))
top_countries.sort_values().plot(kind="barh")
plt.title("Top Revenue Countries")
plt.tight_layout()
plt.savefig("images/top_countries.png")
plt.close()

# -------------------------
# Chart 4 Hourly Orders
# -------------------------
hourly = df.groupby("Hour")["InvoiceNo"].count()

plt.figure(figsize=(8,4))
hourly.plot(marker="o")
plt.title("Orders by Hour")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/hourly_orders.png")
plt.close()

# -------------------------
# Chart 5 Weekday Sales
# -------------------------
weekday = df.groupby("Weekday")["Revenue"].sum().reindex([
    "Monday","Tuesday","Wednesday",
    "Thursday","Friday","Saturday","Sunday"
])

plt.figure(figsize=(8,4))
weekday.plot(kind="bar")
plt.title("Sales by Weekday")
plt.tight_layout()
plt.savefig("images/weekday_sales.png")
plt.close()

# -------------------------
# Chart 6 Customer Distribution
# -------------------------
customer = df.groupby("CustomerID")["Revenue"].sum()

plt.figure(figsize=(8,4))
plt.hist(customer, bins=40)
plt.title("Customer Revenue Distribution")
plt.tight_layout()
plt.savefig("images/customer_distribution.png")
plt.close()

# -------------------------
# Chart 7 Price Distribution
# -------------------------
plt.figure(figsize=(8,4))
plt.hist(df["UnitPrice"], bins=50)
plt.title("Unit Price Distribution")
plt.tight_layout()
plt.savefig("images/price_distribution.png")
plt.close()

# -------------------------
# Chart 8 Quantity Distribution
# -------------------------
plt.figure(figsize=(8,4))
plt.hist(df["Quantity"], bins=50)
plt.title("Quantity Distribution")
plt.tight_layout()
plt.savefig("images/quantity_distribution.png")
plt.close()

print("\nProject Completed Successfully!")

print("\nCharts saved inside 'images/' folder.")