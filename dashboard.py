import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------------------
# LOAD SALES DATA
# ----------------------------------------

sales_df = pd.read_csv("sales.csv")
products_df = pd.read_csv("products.csv")
customers_df = pd.read_csv("customers.csv")


# ----------------------------------------
# PREPARE DATA
# ----------------------------------------

sales_df["order_date"] = pd.to_datetime(sales_df["order_date"])


# Add product information to sales
sales_products = sales_df.merge(
    products_df[
        ["product_id", "product_name", "category"]
    ],
    on="product_id",
    how="left"
)


# Add customer information to sales
sales_full = sales_products.merge(
    customers_df[
        ["customer_id", "city", "region"]
    ],
    on="customer_id",
    how="left"
)


# ----------------------------------------
# CREATE DASHBOARD
# ----------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

fig.suptitle(
    "NEXORA BUSINESS INTELLIGENCE DASHBOARD",
    fontsize=20,
    fontweight="bold"
)


# ----------------------------------------
# CHART 1 — MONTHLY REVENUE
# ----------------------------------------

monthly_revenue = (
    sales_full
    .groupby(
        sales_full["order_date"].dt.to_period("M")
    )["revenue"]
    .sum()
)

axes[0, 0].plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

axes[0, 0].set_title("Monthly Revenue")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue (€)")

axes[0, 0].tick_params(
    axis="x",
    rotation=45
)


# ----------------------------------------
# CHART 2 — REVENUE BY CATEGORY
# ----------------------------------------

category_revenue = (
    sales_full
    .groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

axes[0, 1].bar(
    category_revenue.index,
    category_revenue.values
)

axes[0, 1].set_title("Revenue by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Revenue (€)")

axes[0, 1].tick_params(
    axis="x",
    rotation=45
)


# ----------------------------------------
# CHART 3 — REVENUE BY REGION
# ----------------------------------------

region_revenue = (
    sales_full
    .groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

axes[1, 0].bar(
    region_revenue.index,
    region_revenue.values
)

axes[1, 0].set_title("Revenue by Region")
axes[1, 0].set_xlabel("Region")
axes[1, 0].set_ylabel("Revenue (€)")

axes[1, 0].tick_params(
    axis="x",
    rotation=45
)


# ----------------------------------------
# CHART 4 — TOP 10 PRODUCTS
# ----------------------------------------

top_products = (
    sales_full
    .groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

axes[1, 1].barh(
    top_products.index,
    top_products.values
)

axes[1, 1].set_title("Top 10 Products by Revenue")
axes[1, 1].set_xlabel("Revenue (€)")


# ----------------------------------------
# FINAL LAYOUT
# ----------------------------------------

plt.tight_layout()

plt.savefig(
    "nexora_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("========================================")
print("       NEXORA DASHBOARD")
print("========================================")

print("Dashboard created successfully!")
print("File created: nexora_dashboard.png")