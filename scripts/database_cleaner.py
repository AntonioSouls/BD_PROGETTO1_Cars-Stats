import pandas as pd

print("Starting Dataset Cleaning ...")
# Legge il csv con Pandas e crea una Pandas Table
chunks = pd.read_csv("data/used_cars_data.csv", chunksize=100000, low_memory=False)
df = pd.concat(chunks, ignore_index=True)

# Seleziono le colonne da mantenere e faccio pulizia
print("Selecting the columns to be maintained...")
df = df[["engine_displacement", "horsepower", "make_name", "model_name", "power", "price", "year"]]

print("Removing duplicates ...")
df.drop_duplicates(inplace=True) # Rimuovo i duplicati, ossia righe con stessi valori su tutte le colonne

df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df[df['year'] >= 1000]
df['year'] = df['year'].astype(int)

# Uniformo i nomi
print("Unification of names ...")
df["make_name"] = df["make_name"].str.strip().str.title()
df["model_name"] = df["model_name"].str.strip().str.title()
df["power"] = df["power"].astype(str).str.replace(',','', regex=False).replace('nan', '').str.strip()

# Salvo il DataFrame pulito
df.to_csv("data/vehicles_clean.csv", index=False)
print("Saved cleaned dataset")
