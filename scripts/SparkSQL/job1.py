from pyspark.sql import SparkSession
from pyspark.sql.functions import count, min, max, avg, collect_set, col, concat_ws
import time

# Inizio misurazione tempo
start = time.time()

# Crea la SparkSession
spark = SparkSession.builder \
    .appName("Statistiche Marca-Modello") \
    .getOrCreate()

# Leggi il file CSV da HDFS
df = spark.read.option("header", True).option("inferSchema", True).csv("file:///home/matteo/BD_PROGETTO1_Cars-Stats/data/vehicles_clean.csv")

# Mostra schema per controllo
df.printSchema()

# Raggruppamento e aggregazioni
result = df.groupBy("make_name", "model_name").agg(
    count("*").alias("num_vehicles"),
    min("price").alias("min_price"),
    max("price").alias("max_price"),
    avg("price").alias("avg_price"),
    collect_set("year").alias("years_present")
)

result = result.withColumn("years_present", concat_ws(",", col("years_present")))

# Mostra primi risultati
result.show(10, truncate=False)

# Salva risultato in HDFS
result.write.mode("overwrite").option("header", True).csv("file:///home/matteo/BD_PROGETTO1_Cars-Stats/output/statistiche_marca_modello")

# Fine misurazione tempo
end = time.time()
print(f"Tempo esecuzione: {end - start:.2f} secondi")

# Ferma la sessione
spark.stop()
