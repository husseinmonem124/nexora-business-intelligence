import pandas as pd
import random

# Make the random data reproducible
random.seed(42)


# ----------------------------------------
# CUSTOMER DATA
# ----------------------------------------

first_names = [
    "Lukas", "Anna", "Daniel", "Sophie", "Leon",
    "Emma", "Alexander", "Laura", "Felix", "Marie",
    "Maximilian", "Clara", "Paul", "Hannah", "Jonas",
    "Lena", "Julian", "Lea", "Noah", "Mia"
]

last_names = [
    "Schneider", "Weber", "Fischer", "Wagner", "Müller",
    "Becker", "Hoffmann", "Schäfer", "Koch", "Bauer",
    "Richter", "Klein", "Wolf", "Schröder", "Neumann",
    "Schwarz", "Zimmermann", "Braun", "Krüger", "Hartmann"
]


# ----------------------------------------
# LOCATIONS
# ----------------------------------------

locations = {
    "Berlin": "Berlin",
    "Munich": "Bavaria",
    "Nuremberg": "Bavaria",
    "Augsburg": "Bavaria",
    "Regensburg": "Bavaria",
    "Cologne": "North Rhine-Westphalia",
    "Düsseldorf": "North Rhine-Westphalia",
    "Dortmund": "North Rhine-Westphalia",
    "Essen": "North Rhine-Westphalia",
    "Hamburg": "Hamburg",
    "Frankfurt": "Hesse",
    "Wiesbaden": "Hesse",
    "Stuttgart": "Baden-Württemberg",
    "Mannheim": "Baden-Württemberg",
    "Ulm": "Baden-Württemberg",
    "Freiburg": "Baden-Württemberg",
    "Leipzig": "Saxony",
    "Dresden": "Saxony",
    "Hanover": "Lower Saxony",
    "Braunschweig": "Lower Saxony"
}




customers = []

for number in range(1, 501):

    # Create customer ID
    customer_id = f"C{number:03d}"

    # Select random first and last name
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Combine first and last name
    customer_name = f"{first_name} {last_name}"

    # Select random city
    city = random.choice(list(locations.keys()))

    # Get region for selected city
    region = locations[city]

    # Add customer to the list
    customers.append({
        "customer_id": customer_id,
        "customer_name": customer_name,
        "city": city,
        "region": region
    })


customers_df = pd.DataFrame(customers)



print("First 10 customers:")
print(customers_df.head(10))

print("\n----------------------------------------")

print("Dataset information:")
print(customers_df.info())

print("\n----------------------------------------")

print("Total customers:", len(customers_df))




customers_df.to_csv(
    "customers.csv",
    index=False,
    encoding="utf-8"
)




print("\nCustomer dataset created successfully!")
print("Total customers:", len(customers_df))
print("File created: customers.csv")