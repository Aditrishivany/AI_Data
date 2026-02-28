import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Data from CSV
# -----------------------------
df = pd.read_csv("productsales.csv")

print("\nRaw Data:\n")
print(df)

# -----------------------------
# 2. Data Cleaning
# -----------------------------

# Remove rows where product is missing
df = df.dropna(subset=["product"])

# Convert price and quantity to numeric (handle blanks)
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# Fill missing price with mean price
df["price"].fillna(df["price"].mean(), inplace=True)

# Fill missing quantity with 0
df["quantity"].fillna(0, inplace=True)

print("\nCleaned Data:\n")
print(df)

# -----------------------------
# 3. Create total_sales column
# -----------------------------
df["total_sales"] = df["price"] * df["quantity"]

print("\nData with Total Sales:\n")
print(df)

# -----------------------------
# 4. Total Sales Per Product
# -----------------------------
sales_per_product = df.groupby("product")["total_sales"].sum()

print("\nTotal Sales Per Product:\n")
print(sales_per_product)

# -----------------------------
# 5. Best Selling Product
# -----------------------------
best_product = sales_per_product.idxmax()
print("\nBest Selling Product:", best_product)

# -----------------------------
# 6. Total Sales Per Day
# -----------------------------
sales_per_day = df.groupby("day")["total_sales"].sum()

print("\nTotal Sales Per Day:\n")
print(sales_per_day)

# -----------------------------
# 7. Visualization (Bar Chart)
# -----------------------------
sales_per_day.plot(kind="bar")

plt.title("Total Sales Per Day")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

# NON-BLOCKING SHOW (Fixes freezing)
plt.show(block=False)
plt.pause(3)   # Show chart for 3 seconds
plt.close()    # Auto-close chart window
