import pandas as pd
import random

# Make the random data reproducible

random.seed(42)

# ----------------------------------------

# PRODUCT DATA

# ----------------------------------------

products = [

# Computers
("Dell Inspiron 15", "Computers", "Dell", 749, 580),
("HP Pavilion 15", "Computers", "HP", 699, 540),
("Lenovo IdeaPad 5", "Computers", "Lenovo", 649, 500),
("ASUS VivoBook 15", "Computers", "ASUS", 679, 520),
("Apple MacBook Air", "Computers", "Apple", 1199, 900),
("Acer Aspire 5", "Computers", "Acer", 599, 450),
("Lenovo ThinkPad E14", "Computers", "Lenovo", 899, 690),

# Tablets
("Apple iPad 10", "Tablets", "Apple", 449, 340),
("Samsung Galaxy Tab S9", "Tablets", "Samsung", 799, 610),
("Lenovo Tab P12", "Tablets", "Lenovo", 399, 300),
("Xiaomi Pad 6", "Tablets", "Xiaomi", 349, 260),
("Apple iPad Air", "Tablets", "Apple", 699, 530),

# Nintendo Switch
("Nintendo Switch OLED", "Nintendo Switch", "Nintendo", 349, 270),
("Nintendo Switch", "Nintendo Switch", "Nintendo", 299, 230),
("Nintendo Switch Lite", "Nintendo Switch", "Nintendo", 219, 170),
("Nintendo Switch 2", "Nintendo Switch", "Nintendo", 449, 350),

# Monitors
("Samsung 27-inch Monitor", "Monitors", "Samsung", 249, 180),
("LG UltraGear 27", "Monitors", "LG", 329, 240),
("Dell 24-inch Monitor", "Monitors", "Dell", 189, 140),
("ASUS TUF Gaming Monitor", "Monitors", "ASUS", 379, 280),
("AOC 27-inch Gaming Monitor", "Monitors", "AOC", 299, 220),
("Samsung Odyssey G7", "Monitors", "Samsung", 649, 490),

# Smartphones
("iPhone 15", "Smartphones", "Apple", 799, 610),
("iPhone 15 Pro", "Smartphones", "Apple", 1199, 920),
("iPhone 16", "Smartphones", "Apple", 899, 690),
("Samsung Galaxy S24", "Smartphones", "Samsung", 899, 680),
("Samsung Galaxy S24 Ultra", "Smartphones", "Samsung", 1299, 990),
("Google Pixel 9", "Smartphones", "Google", 799, 600),
("Xiaomi 14", "Smartphones", "Xiaomi", 699, 520),

# PlayStation
("PlayStation 5 Slim", "PlayStation", "Sony", 549, 420),
("PlayStation 5 Digital", "PlayStation", "Sony", 449, 345),
("PlayStation 5 Pro", "PlayStation", "Sony", 799, 620),

# Xbox
("Xbox Series X", "Xbox", "Microsoft", 549, 420),
("Xbox Series S", "Xbox", "Microsoft", 299, 225),
("Xbox Series X 2TB", "Xbox", "Microsoft", 649, 500),

# Accessories
("Apple Magic Mouse", "Accessories", "Apple", 89, 55),
("Logitech MX Master 3S", "Accessories", "Logitech", 109, 70),
("Logitech K380 Keyboard", "Accessories", "Logitech", 49, 30),
("Samsung Wireless Charger", "Accessories", "Samsung", 39, 22),
("Apple USB-C Cable", "Accessories", "Apple", 25, 12),
("Sony DualSense Controller", "Accessories", "Sony", 74, 48),
("Xbox Wireless Controller", "Accessories", "Microsoft", 69, 45),
("Nintendo Switch Pro Controller", "Accessories", "Nintendo", 79, 50),
("Gaming Headset", "Accessories", "Logitech", 99, 60),
("HDMI Cable", "Accessories", "Generic", 19, 8),
("External SSD 1TB", "Accessories", "Samsung", 99, 65),
("Power Bank 20000mAh", "Accessories", "Anker", 49, 30),
("USB-C Hub", "Accessories", "Anker", 59, 35),
("Webcam 1080p", "Accessories", "Logitech", 69, 42),
("Mechanical Gaming Keyboard", "Accessories", "Logitech", 129, 80),
("Gaming Mouse", "Accessories", "Logitech", 59, 35)


]

# ----------------------------------------

# CREATE PRODUCT RECORDS

# ----------------------------------------

product_records = []

for number, product in enumerate(products, start=1):

    product_id = f"P{number:03d}"

    product_name = product[0]
    category = product[1]
    brand = product[2]
    price = product[3]
    cost = product[4]

    stock = random.randint(5, 100)

    product_records.append({
    "product_id": product_id,
    "product_name": product_name,
    "category": category,
    "brand": brand,
    "price": price,
    "cost": cost,
    "stock": stock
})


# ----------------------------------------

# CREATE DATAFRAME

# ----------------------------------------

products_df = pd.DataFrame(product_records)

# ----------------------------------------

# CALCULATE PROFIT

# ----------------------------------------

products_df["profit_per_unit"] = (
products_df["price"] - products_df["cost"]
)

# ----------------------------------------

# DISPLAY DATA

# ----------------------------------------

print("First 10 products:")
print(products_df.head(10))

print("\n----------------------------------------")

print("Dataset information:")
print(products_df.info())

print("\n----------------------------------------")

print("Total products:", len(products_df))

# ----------------------------------------

# SAVE AS CSV

# ----------------------------------------

products_df.to_csv(
"products.csv",
index=False,
encoding="utf-8"
)

print("\nProduct dataset created successfully!")
print("Total products:", len(products_df))
print("File created: products.csv")
