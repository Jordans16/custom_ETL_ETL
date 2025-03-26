import pandas as pd
from faker import Faker
import random

fake = Faker()

# Générer des données de vente e-commerce
data = []
for _ in range(1000):
    data.append({
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "customer_email": fake.email(),
        "product": fake.word(),
        "category": random.choice(["Electronics", "Clothing", "Home", "Beauty"]),
        "price": round(random.uniform(5, 500), 2),
        "quantity": random.randint(1, 5),
        "total": round(random.uniform(5, 500) * random.randint(1, 5), 2),
        "date": fake.date_this_decade()
    })

df = pd.DataFrame(data)
df.to_csv("fake_shopify_data.csv", index=False)
print("✅ Dataset Shopify simulé et exporté !")
