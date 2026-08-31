import pandas as pd
import random

# Make the random data reproducible

random.seed(42)

# ----------------------------------------

# LOAD EXISTING DATASETS

# ----------------------------------------

customers_df = pd.read_csv("customers.csv")
products_df = pd.read_csv("products.csv")

# ----------------------------------------

# GENERATE SALES DATA

# ----------------------------------------

sales = []

for number in range(1, 2001):
# Create order ID
    order_id = f"O{number:04d}"

# Select random customer
    customer = customers_df.sample(1).iloc[0]

    customer_id = customer["customer_id"]

# Select random product
    product = products_df.sample(1).iloc[0]

    product_id = product["product_id"]

# Product information
    unit_price = product["price"]
    unit_cost = product["cost"]

# Random quantity
    quantity = random.randint(1, 5)

# Random order date
    order_date = pd.Timestamp(
    "2025-01-01"
) + pd.Timedelta(
    days=random.randint(0, 364)
)

# Calculate financial values
    revenue = unit_price * quantity
    cost = unit_cost * quantity
    profit = revenue - cost

# Add sale
    sales.append({
    "order_id": order_id,
    "customer_id": customer_id,
    "product_id": product_id,
    "order_date": order_date,
    "quantity": quantity,
    "unit_price": unit_price,
    "unit_cost": unit_cost,
    "revenue": revenue,
    "cost": cost,
    "profit": profit
})


# ----------------------------------------

# CREATE DATAFRAME

# ----------------------------------------

sales_df = pd.DataFrame(sales)

# ----------------------------------------

# DISPLAY DATA

# ----------------------------------------

print("First 10 sales:")
print(sales_df.head(10))

print("\n----------------------------------------")

print("Dataset information:")
print(sales_df.info())

print("\n----------------------------------------")

print("Total orders:", len(sales_df))

print("Total items sold:", sales_df["quantity"].sum())

print(
f"Total revenue: €{sales_df['revenue'].sum():,.2f}"
)

print(
f"Total profit: €{sales_df['profit'].sum():,.2f}"
)

# ----------------------------------------

# SAVE AS CSV

# ----------------------------------------

sales_df.to_csv(
"sales.csv",
index=False,
encoding="utf-8"
)

print("\nSales dataset created successfully!")
print("Total orders:", len(sales_df))
print("File created: sales.csv")
