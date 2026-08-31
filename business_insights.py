import pandas as pd


# ----------------------------------------
# LOAD DATA
# ----------------------------------------

sales_df = pd.read_csv("sales.csv")
products_df = pd.read_csv("products.csv")
customers_df = pd.read_csv("customers.csv")


# ----------------------------------------
# CONNECT SALES WITH PRODUCT DATA
# ----------------------------------------

sales_with_products = sales_df.merge(
    products_df,
    on="product_id",
    how="left"
)


# ----------------------------------------
# CONNECT SALES WITH CUSTOMER DATA
# ----------------------------------------

sales_full = sales_with_products.merge(
    customers_df,
    on="customer_id",
    how="left"
)


# ----------------------------------------
# BUSINESS INSIGHTS
# ----------------------------------------

print("========================================")
print("       NEXORA BUSINESS INSIGHTS")
print("========================================")


# ----------------------------------------
# INSIGHT 1 — TOP REVENUE CATEGORY
# ----------------------------------------

category_revenue = (
    sales_full
    .groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_category = category_revenue.index[0]
top_category_revenue = category_revenue.iloc[0]

print("\n1. TOP REVENUE CATEGORY")
print("----------------------------------------")
print(f"{top_category} generated the highest revenue.")
print(f"Revenue: €{top_category_revenue:,.2f}")


# ----------------------------------------
# INSIGHT 2 — HIGHEST PROFIT MARGIN
# ----------------------------------------

category_profit = (
    sales_full
    .groupby("category")
    .agg(
        revenue=("revenue", "sum"),
        profit=("profit", "sum")
    )
)

category_profit["profit_margin"] = (
    category_profit["profit"]
    / category_profit["revenue"]
    * 100
)

highest_margin_category = (
    category_profit["profit_margin"]
    .idxmax()
)

highest_margin = (
    category_profit["profit_margin"]
    .max()
)

print("\n2. HIGHEST PROFIT MARGIN")
print("----------------------------------------")
print(f"{highest_margin_category} has the highest profit margin.")
print(f"Profit margin: {highest_margin:.2f}%")


# ----------------------------------------
# INSIGHT 3 — TOP CITY
# ----------------------------------------

city_revenue = (
    sales_full
    .groupby("city")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_city = city_revenue.index[0]
top_city_revenue = city_revenue.iloc[0]

print("\n3. TOP REVENUE CITY")
print("----------------------------------------")
print(f"{top_city} generated the highest revenue.")
print(f"Revenue: €{top_city_revenue:,.2f}")


# ----------------------------------------
# INSIGHT 4 — TOP REGION
# ----------------------------------------

region_revenue = (
    sales_full
    .groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_region = region_revenue.index[0]
top_region_revenue = region_revenue.iloc[0]

print("\n4. TOP REVENUE REGION")
print("----------------------------------------")
print(f"{top_region} generated the highest revenue.")
print(f"Revenue: €{top_region_revenue:,.2f}")


# ----------------------------------------
# INSIGHT 5 — BEST MONTH
# ----------------------------------------

sales_full["order_date"] = pd.to_datetime(
    sales_full["order_date"]
)

monthly_revenue = (
    sales_full
    .assign(
        month=sales_full["order_date"]
        .dt.to_period("M")
        .astype(str)
    )
    .groupby("month")["revenue"]
    .sum()
)

best_month = monthly_revenue.idxmax()
best_month_revenue = monthly_revenue.max()

print("\n5. BEST REVENUE MONTH")
print("----------------------------------------")
print(f"{best_month} generated the highest monthly revenue.")
print(f"Revenue: €{best_month_revenue:,.2f}")


# ----------------------------------------
# FINAL SUMMARY
# ----------------------------------------

print("\n========================================")
print("       MANAGEMENT SUMMARY")
print("========================================")

print(f"""
Nexora generated €{sales_full["revenue"].sum():,.2f}
in total revenue during 2025.

The strongest revenue category was {top_category}.

The highest-margin category was
{highest_margin_category} at {highest_margin:.2f}%.

The strongest city was {top_city}.

The strongest region was {top_region}.

The strongest month was {best_month}.
""")