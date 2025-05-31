import pandas as pd

# Legge il csv con Pandas e crea una Pandas Table
df = pd.read_csv("data/used_cars_data.csv")

# Seleziono le colonne da mantenere e faccio pulizia
df = df[["engine_displacement", "horsepower", "make_name", "model_name", "power", "price", "year"]]
df.dropna(subset=["make_name", "model_name", "price", "year", "horsepower", "engine_displacement"], inplace=True) # Elimino le righe che hanno NaN in almeno una di queste colonne
df.drop_duplicates(inplace=True) # Rimuovo i duplicati, ossia righe con stessi valori su tutte le colonne

# Rimuovo eventuali valori improbabili
df = df[df["price"] > 500]
df = df[(df["year"] >= 1980)]
df = df[(df["horsepower"] > 20) & (df["horsepower"] < 1500)]

# Uniformo i nomi
df["make_name"] = df["make_name"].str.strip().str.title()
df["model_name"] = df["model_name"].str.strip().str.title()

# Saalvo il DataFrame pulito
df.to_csv("data/vehicles_clean.csv", index=False)

