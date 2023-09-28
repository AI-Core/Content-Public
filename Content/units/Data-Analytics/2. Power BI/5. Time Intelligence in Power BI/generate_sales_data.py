#%%
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate a random date between two dates
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Set the seed for reproducibility
random.seed(42)

# Number of rows
n = 300

# Date range
start_date = datetime.strptime("01/01/2020", "%d/%m/%Y")
end_date = datetime.strptime("30/09/2023", "%d/%m/%Y")

# Product IDs
products = [f"P{str(i).zfill(3)}" for i in range(1, 11)]

# Unit price by product ID
prices = {product: random.randint(10, 200) for product in products}

# Generate the sales data
data = {
    "Order date": [random_date(start_date, end_date).strftime("%d/%m/%Y") for _ in range(n)],
    "Product ID": [random.choice(products) for _ in range(n)],
    "Order quantity": [random.randint(1, 20) for _ in range(n)],
    "Unit price": []
}

# Populate unit price based on product ID
for prod in data["Product ID"]:
    data["Unit price"].append(prices[prod])

# Create the dataframe
df = pd.DataFrame(data)

# Save to a CSV file if needed
# df.to_csv("sales_data.csv", index=False)

df.to_csv('timeintelligence_sales_data.csv', index=False)

# %%
