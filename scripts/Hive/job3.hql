-- Parametri Hive
SET hive.strict.checks.cartesian.product=false;
SET hive.mapred.mode=nonstrict;

-- Step 0: crea tabella
DROP TABLE IF EXISTS cars;

CREATE EXTERNAL TABLE IF NOT EXISTS cars (
  engine_displacement FLOAT,
  horsepower FLOAT,
  make_name STRING,
  model_name STRING,
  power FLOAT,
  price FLOAT,
  year INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/frompoo/data';

-- Step 1: crea tabella con bucket_id
DROP TABLE IF EXISTS cars_bucketed;

CREATE TABLE cars_bucketed AS
SELECT
  *,
  CAST(FLOOR(engine_displacement / 0.2) AS INT) * 1000 + CAST(FLOOR(horsepower / 10) AS INT) AS bucket_id
FROM cars;

-- Step 2: join solo tra modelli nello stesso bucket
DROP TABLE IF EXISTS cars_joined;

CREATE TABLE cars_joined AS
SELECT
  a.model_name AS group_rep,
  b.model_name AS grouped_model,
  b.horsepower,
  b.engine_displacement,
  b.price
FROM cars_bucketed a
JOIN cars_bucketed b
  ON a.bucket_id = b.bucket_id
WHERE
  ABS(a.horsepower - b.horsepower)/a.horsepower <= 0.1
  AND ABS(a.engine_displacement - b.engine_displacement)/a.engine_displacement <= 0.1;

-- Step 3: aggregazioni finali
INSERT OVERWRITE DIRECTORY '/user/frompoo/data/output_job3_Hive'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
  group_rep,
  ROUND(AVG(price), 2) AS avg_price,
  MAX(horsepower) AS max_hp,
  CONCAT_WS(',', COLLECT_SET(grouped_model)) AS grouped_models
FROM cars_joined
GROUP BY group_rep;
