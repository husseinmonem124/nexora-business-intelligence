import pandas as pd


# ----------------------------------------
# LOAD SALES DATA
# ----------------------------------------

sales_df = pd.read_csv("sales.csv")


# ----------------------------------------
# BASIC BUSINESS KPIs
# ----------------------------------------

total_orders = len(sales_df)

total_items_sold = sales_df["quantity"].sum()

total_revenue = sales_df["revenue"].sum()

total_cost = sales_df["cost"].sum()

total_profit = sales_df["profit"].sum()


# ----------------------------------------
# PROFIT MARGIN
# ----------------------------------------

profit_margin = (total_profit / total_revenue) * 100


# ----------------------------------------
# DISPLAY RESULTS
# ----------------------------------------

print("========================================")
print("       NEXORA BUSINESS ANALYSIS")
print("========================================")

print("\nBUSINESS KPIs")

print("Total Orders:", total_orders)

print("Total Items Sold:", total_items_sold)

print(f"Total Revenue: €{total_revenue:,.2f}")

print(f"Total Cost: €{total_cost:,.2f}")

print(f"Total Profit: €{total_profit:,.2f}")

print(f"Profit Margin: {profit_margin:.2f}%")

# ----------------------------------------
# REVENUE & PROFIT BY CATEGORY
# ----------------------------------------

products_df = pd.read_csv("products.csv")

category_analysis = sales_df.merge(
    products_df[["product_id", "category"]],
    on="product_id",
    how="left"
)

category_summary = (
    category_analysis
    .groupby("category")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )
    .sort_values("revenue", ascending=False)
)


print("\n========================================")
print("       REVENUE & PROFIT BY CATEGORY")
print("========================================")

print(category_summary)

# ----------------------------------------
# TOP PRODUCTS BY REVENUE
# ----------------------------------------

product_analysis = (
    sales_df
    .merge(
        products_df[
            ["product_id", "product_name", "category", "brand"]
        ],
        on="product_id",
        how="left"
    )
)

product_summary = (
    product_analysis
    .groupby(
        ["product_id", "product_name", "category", "brand"]
    )
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )
    .sort_values("revenue", ascending=False)
)


print("\n========================================")
print("       TOP PRODUCTS BY REVENUE")
print("========================================")

print(product_summary.head(10))

# ----------------------------------------
# PROFIT MARGIN BY CATEGORY
# ----------------------------------------

category_summary["profit_margin"] = (
    category_summary["profit"]
    / category_summary["revenue"]
) * 100

category_summary = category_summary.sort_values(
    "profit_margin",
    ascending=False
)


print("\n========================================")
print("       PROFIT MARGIN BY CATEGORY")
print("========================================")

print(
    category_summary[
        ["revenue", "profit", "units_sold", "profit_margin"]
    ]
)

# ----------------------------------------
# MONTHLY SALES ANALYSIS
# ----------------------------------------

sales_df["order_date"] = pd.to_datetime(sales_df["order_date"])

sales_df["month"] = sales_df["order_date"].dt.to_period("M")

monthly_summary = (
    sales_df
    .groupby("month")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
        units_sold=("quantity", "sum")
    )
)

print("\n========================================")
print("       MONTHLY SALES ANALYSIS")
print("========================================")

print(monthly_summary)

# ----------------------------------------
# CUSTOMER ANALYSIS
# ----------------------------------------

customers_df = pd.read_csv("customers.csv")

customer_analysis = sales_df.merge(
    customers_df[
        ["customer_id", "customer_name", "city", "region"]
    ],
    on="customer_id",
    how="left"
)


# ----------------------------------------
# CUSTOMER SUMMARY
# ----------------------------------------

customer_summary = (
    customer_analysis
    .groupby(
        ["customer_id", "customer_name", "city", "region"]
    )
    .agg(
        orders=("order_id", "count"),
        items_purchased=("quantity", "sum"),
        total_spent=("revenue", "sum"),
        total_profit=("profit", "sum")
    )
    .sort_values("total_spent", ascending=False)
)


# ----------------------------------------
# TOP CUSTOMERS
# ----------------------------------------

print("\n========================================")
print("       TOP CUSTOMERS BY SPENDING")
print("========================================")

print(customer_summary.head(10))
# ----------------------------------------
# REVENUE BY CITY
# ----------------------------------------

city_summary = (
    customer_analysis
    .groupby("city")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
        units_sold=("quantity", "sum")
    )
    .sort_values("revenue", ascending=False)
)


# ----------------------------------------
# DISPLAY CITY ANALYSIS
# ----------------------------------------

print("\n========================================")
print("       REVENUE BY CITY")
print("========================================")

print(city_summary)

# ----------------------------------------
# REVENUE BY REGION
# ----------------------------------------

region_summary = (
    customer_analysis
    .groupby("region")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "count"),
        units_sold=("quantity", "sum")
    )
    .sort_values("revenue", ascending=False)
)


# ----------------------------------------
# DISPLAY REGION ANALYSIS
# ----------------------------------------

print("\n========================================")
print("       REVENUE BY REGION")
print("========================================")

print(region_summary)

# ----------------------------------------
# REVENUE BY CATEGORY CHART
# ----------------------------------------

import matplotlib.pyplot as plt

# Connect sales data with product information
sales_with_products = sales_df.merge(
    products_df[["product_id", "category"]],
    on="product_id",
    how="left"
)

# Calculate revenue by category
category_revenue = (
    sales_with_products
    .groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Create chart
plt.figure(figsize=(10, 6))

category_revenue.plot(kind="bar")

plt.title("Nexora Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue (€)")

plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("revenue_by_category.png")

# Display chart
plt.show()
# ----------------------------------------
# MONTHLY REVENUE CHART
# ----------------------------------------

monthly_revenue = (
    sales_df
    .assign(month=sales_df["order_date"].dt.to_period("M").astype(str))
    .groupby("month")["revenue"]
    .sum()
)

plt.figure(figsize=(10, 6))

monthly_revenue.plot(kind="line", marker="o")

plt.title("Nexora Monthly Revenue — 2025")
plt.xlabel("Month")
plt.ylabel("Revenue (€)")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig("monthly_revenue.png")

# Display chart
plt.show()

# ----------------------------------------
# PROFIT BY CATEGORY CHART
# ----------------------------------------

category_profit = (
    sales_with_products
    .groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_profit.plot(kind="bar")

plt.title("Nexora Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Profit (€)")

plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("profit_by_category.png")

# Display chart
plt.show()