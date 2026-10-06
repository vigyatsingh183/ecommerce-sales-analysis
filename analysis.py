import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

print("===== E-COMMERCE SALES ANALYSIS =====")

print("\nTotal Revenue:")
print(f"₹{df['Revenue'].sum():,.2f}")

print("\nTotal Units Sold:")
print(df["Quantity"].sum())

print("\nRevenue by Category:")
print(
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 5 Products:")
print(
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Monthly sales
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_sales)

# Category chart
category_sales = df.groupby("Category")["Revenue"].sum()

category_sales.plot(
    kind="bar",
    title="Revenue by Category"
)

plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()

# Monthly trend
monthly_sales.astype(float).plot(
    kind="line",
    marker="o",
    title="Monthly Revenue Trend"
)

plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()
