DROP TABLE IF EXISTS cars;

-- Crea la tabella esterna

CREATE EXTERNAL TABLE IF NOT EXISTS cars (
  make_name STRING,
  model_name STRING,
  year INT,
  price FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/frompoo/data';

-- Job 1: Statistiche per ogni marca e modello
-- Risultato: elenco di marche, modelli, numero di auto, min/max/media dei prezzi e anni in cui compaiono

INSERT OVERWRITE DIRECTORY '/user/frompoo/data/output_job1_Hive'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
  make_name,
  model_name,
  COUNT(*) AS num_cars,
  MIN(price) AS min_price,
  MAX(price) AS max_price,
  ROUND(AVG(price), 2) AS avg_price,
  COLLECT_SET(year) AS years
FROM cars
GROUP BY make_name, model_name;
