import sqlite3
import pandas as pd


# ----------------------------------------
# CONNECT TO DATABASE
# ----------------------------------------

connection = sqlite3.connect("nexora.db")


# ----------------------------------------
# LOAD CSV DATA
# ----------------------------------------

customers_df = pd.read_csv("customers.csv")
products_df = pd.read_csv("products.csv")
sales_df = pd.read_csv("sales.csv")


# ----------------------------------------
# SAVE DATA INTO SQLITE TABLES
# ----------------------------------------

customers_df.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False
)

products_df.to_sql(
    "products",
    connection,
    if_exists="replace",
    index=False
)

sales_df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)


# ----------------------------------------
# CONFIRM DATABASE
# ----------------------------------------

print("========================================")
print("       NEXORA SQL DATABASE")
print("========================================")

print("\nDatabase created successfully!")

print("\nTables created:")
print("- customers")
print("- products")
print("- sales")


# ----------------------------------------
# CHECK NUMBER OF RECORDS
# ----------------------------------------

customers_count = pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM customers",
    connection
)

products_count = pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM products",
    connection
)

sales_count = pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM sales",
    connection
)


print("\nRecord counts:")
print("Customers:", customers_count.iloc[0]["total"])
print("Products:", products_count.iloc[0]["total"])
print("Sales:", sales_count.iloc[0]["total"])

# ----------------------------------------
# SQL QUERY — BUSINESS KPIs
# ----------------------------------------

query = """
SELECT
    SUM(revenue) AS total_revenue,
    SUM(cost) AS total_cost,
    SUM(profit) AS total_profit
FROM sales
"""

result = pd.read_sql_query(query, connection)

total_revenue = result.iloc[0]["total_revenue"]
total_cost = result.iloc[0]["total_cost"]
total_profit = result.iloc[0]["total_profit"]

profit_margin = (
    total_profit / total_revenue
) * 100


print("\n========================================")
print("       SQL — BUSINESS KPIs")
print("========================================")

print(f"Total Revenue: €{total_revenue:,.2f}")
print(f"Total Cost: €{total_cost:,.2f}")
print(f"Total Profit: €{total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")

# ----------------------------------------
# SQL QUERY — REVENUE BY CATEGORY
# ----------------------------------------

query = """
SELECT
    products.category,
    SUM(sales.revenue) AS revenue,
    SUM(sales.profit) AS profit,
    SUM(sales.quantity) AS units_sold
FROM sales
JOIN products
    ON sales.product_id = products.product_id
GROUP BY products.category
ORDER BY revenue DESC
"""

category_result = pd.read_sql_query(
    query,
    connection
)

print("\n========================================")
print("       SQL — REVENUE BY CATEGORY")
print("========================================")

print(category_result)
# ----------------------------------------
# CLOSE DATABASE
# ----------------------------------------
# ----------------------------------------
# SQL QUERY — TOP 10 PRODUCTS BY REVENUE
# ----------------------------------------

query = """
SELECT
    products.product_id,
    products.product_name,
    products.category,
    products.brand,
    SUM(sales.revenue) AS revenue,
    SUM(sales.profit) AS profit,
    SUM(sales.quantity) AS units_sold
FROM sales
JOIN products
    ON sales.product_id = products.product_id
GROUP BY
    products.product_id,
    products.product_name,
    products.category,
    products.brand
ORDER BY revenue DESC
LIMIT 10
"""

top_products = pd.read_sql_query(
    query,
    connection
)

print("\n========================================")
print("       SQL — TOP 10 PRODUCTS")
print("========================================")

print(top_products)

# ----------------------------------------
# SQL QUERY — TOP 10 CUSTOMERS BY SPENDING
# ----------------------------------------

query = """
SELECT
    customers.customer_id,
    customers.customer_name,
    customers.city,
    customers.region,
    SUM(sales.revenue) AS total_spent,
    COUNT(sales.order_id) AS number_of_orders,
    SUM(sales.quantity) AS items_purchased
FROM sales
JOIN customers
    ON sales.customer_id = customers.customer_id
GROUP BY
    customers.customer_id,
    customers.customer_name,
    customers.city,
    customers.region
ORDER BY total_spent DESC
LIMIT 10
"""

top_customers = pd.read_sql_query(
    query,
    connection
)

print("\n========================================")
print("       SQL — TOP 10 CUSTOMERS")
print("========================================")

print(top_customers)

# ----------------------------------------
# SQL QUERY — REVENUE BY CITY
# ----------------------------------------

query = """
SELECT
    customers.city,
    SUM(sales.revenue) AS revenue,
    SUM(sales.profit) AS profit,
    COUNT(sales.order_id) AS orders,
    SUM(sales.quantity) AS units_sold
FROM sales
JOIN customers
    ON sales.customer_id = customers.customer_id
GROUP BY customers.city
ORDER BY revenue DESC
"""

city_result = pd.read_sql_query(
    query,
    connection
)

print("\n========================================")
print("       SQL — REVENUE BY CITY")
print("========================================")

print(city_result)

# ----------------------------------------
# SQL QUERY — REVENUE BY REGION
# ----------------------------------------

query = """
SELECT
    customers.region,
    SUM(sales.revenue) AS revenue,
    SUM(sales.profit) AS profit,
    COUNT(sales.order_id) AS orders,
    SUM(sales.quantity) AS units_sold
FROM sales
JOIN customers
    ON sales.customer_id = customers.customer_id
GROUP BY customers.region
ORDER BY revenue DESC
"""

region_result = pd.read_sql_query(
    query,
    connection
)

print("\n========================================")
print("       SQL — REVENUE BY REGION")
print("========================================")

print(region_result)

# ----------------------------------------
# SQL QUERY — MONTHLY SALES ANALYSIS
# ----------------------------------------

query = """
SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(revenue) AS revenue,
    SUM(profit) AS profit,
    COUNT(order_id) AS orders,
    SUM(quantity) AS units_sold
FROM sales
GROUP BY month
ORDER BY month
"""

monthly_result = pd.read_sql_query(
    query,
    connection
)

print("\n========================================")
print("       SQL — MONTHLY SALES")
print("========================================")

print(monthly_result)

connection.close()

print("\nDatabase connection closed.")