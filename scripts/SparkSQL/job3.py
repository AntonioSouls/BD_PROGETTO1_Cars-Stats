from pyspark.sql import SparkSession
from pyspark.sql.functions import col, floor, avg, max

# Avvia SparkSession
spark = SparkSession.builder \
    .appName("Gruppi di modelli con motori simili") \
    .getOrCreate()

# Carica il dataset
df = spark.read.csv("file:///home/matteo/BD_PROGETTO1_Cars-Stats/data/vehicles_clean.csv", header=True, inferSchema=True)

# Filtra i campi necessari e rimuovi i valori nulli
df = df.select("make_name", "model_name", "horsepower", "engine_displacement", "price") \
       .dropna(subset=["model_name", "horsepower", "engine_displacement", "price"])

# Arrotonda horsepower e cilindrata al 10% per identificare gruppi "simili"
df = df.withColumn("hp_group", floor(col("horsepower") / 10)) \
       .withColumn("disp_group", floor(col("engine_displacement") / 10)) \
       .withColumn("group_id", (col("hp_group") * 1000 + col("disp_group")).cast("int"))

# Calcola il prezzo medio e la potenza massima per ciascun gruppo
grouped = df.groupBy("group_id") \
    .agg(
        avg("price").alias("avg_price"),
        max("horsepower").alias("max_hp")
    )

max_hp_df = df.select("group_id", "model_name", "horsepower") \
              .join(grouped.select(col("group_id"), col("max_hp").alias("group_max_hp")), on="group_id") \
              .where(col("horsepower") == col("group_max_hp")) \
              .dropDuplicates(["group_id"])

final_result = grouped \
    .join(max_hp_df.select("group_id", "model_name"), on="group_id") \
    .select("group_id", "avg_price", "max_hp", "model_name")


# Salva l'output
final_result.write.mode("overwrite").option("header", True).csv("file:///home/matteo/BD_PROGETTO1_Cars-Stats/output/gruppi_modelli_simili")

# Chiude la sessione Spark
spark.stop()
