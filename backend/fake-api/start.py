from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI()
faker = Faker()

file_name = "backend/fake-api/products.csv"

df = pd.read_csv(file_name)
df["indice"] = range(1, len(df) + 1)
df.set_index("indice", inplace=True)

@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df) - 1)
    row = df.iloc[index]
    price_with_dot = row["Price"].replace(',', '.') 
    return [
        {
            "client": faker.name(),
            "creditcard": faker.credit_card_provider(),
            "product": row["Product Name"],
            "ean": int(row["EAN"]),
            "price": round(float(price_with_dot) * 1.2, 2),
            "clientPosition": faker.location_on_land(),
            "store": 11,
            "dateTime": faker.iso8601(),
        }
    ]

@app.get("/gerar_compras/{numero_registro}")
async def gerar_compra(numero_registro: int):
    if numero_registro < 1:
        return {"error": "O número deve ser maior que 1"}

    respostas = []

    for _ in range(numero_registro):
        index = random.randint(1, len(df) - 1)
        row = df.iloc[index]
        price_with_dot = row["Price"].replace(',', '.') 
        compra = {
            "client": faker.name(),
            "creditcard": faker.credit_card_provider(),
            "product": row["Product Name"],
            "ean": int(row["EAN"]),
            "price": round(float(price_with_dot) * 1.2, 2),  # Converte para float após substituição
            "clientPosition": faker.location_on_land(),
            "store": 11,
            "dateTime": faker.iso8601(),
        }
        respostas.append(compra)

    return respostas