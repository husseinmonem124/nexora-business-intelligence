import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------------------
# LOAD SALES DATA
# ----------------------------------------

sales_df = pd.read_csv("sales.csv")

sales_df["order_date"] = pd.to_datetime(
    sales_df["order_date"]
)


# ----------------------------------------
# MONTHLY REVENUE
# ----------------------------------------

sales_df["month"] = sales_df["order_date"].dt.to_period("M")

monthly_revenue = (
    sales_df
    .groupby("month")["revenue"]
    .sum()
)


# ----------------------------------------
# CREATE CHART
# ----------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Nexora Monthly Revenue — 2025")

plt.xlabel("Month")

plt.ylabel("Revenue (€)")

plt.xticks(rotation=45)

plt.tight_layout()


# ----------------------------------------
# SAVE CHART
# ----------------------------------------

plt.savefig(
    "monthly_revenue.png",
    dpi=300
)

plt.show()

print("Monthly revenue chart created successfully!")

# ----------------------------------------
# REVENUE BY CATEGORY
# ----------------------------------------

products_df = pd.read_csv("products.csv")

category_analysis = sales_df.merge(
    products_df[["product_id", "category"]],
    on="product_id",
    how="left"
)

category_revenue = (
    category_analysis
    .groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)


# ----------------------------------------
# CREATE CATEGORY CHART
# ----------------------------------------

plt.figure(figsize=(10, 6))

category_revenue.plot(
    kind="bar"
)

plt.title("Nexora Revenue by Product Category")

plt.xlabel("Category")

plt.ylabel("Revenue (€)")

plt.xticks(rotation=45)

plt.tight_layout()


# ----------------------------------------
# SAVE CHART
# ----------------------------------------

plt.savefig(
    "revenue_by_category.png",
    dpi=300
)

plt.show()

print("Category revenue chart created successfully!")