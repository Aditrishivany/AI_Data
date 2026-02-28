import pandas as pd

# Load dataset
df = pd.read_csv("sales.csv")
print("Sales Data:")
print(df)

# Calculate total sales = price * quantity
df["total_sales"] = df["price"] * df["quantity"]

# 1) Total sales per product
total_sales_per_product = df.groupby("product")["total_sales"].sum()
print("\nTotal Sales Per Product:")
print(total_sales_per_product)

# 2) Best-selling product (by quantity)
best_by_quantity = df.groupby("product")["quantity"].sum().idxmax()
print("\nBest Selling (Most Quantity Sold):", best_by_quantity)

# 3) Add tax column (20%)
df["tax_20_percent"] = df["total_sales"] * 0.20

print("\nFinal Data:")
print(df)
