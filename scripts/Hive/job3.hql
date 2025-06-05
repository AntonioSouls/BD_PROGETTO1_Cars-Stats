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

-- Step 1: crea una tabella temporanea con i gruppi distinti
DROP TABLE IF EXISTS car_groups;

CREATE TABLE car_groups AS
SELECT DISTINCT
  engine_displacement,
  horsepower,
  power,
  ROW_NUMBER() OVER () AS group_id
FROM cars;

-- Step 2: join tra cars e car_groups per assegnare ogni modello a un gruppo
DROP TABLE IF EXISTS cars_with_group;

CREATE TABLE cars_with_group AS
SELECT
  c.*,
  g.group_id
FROM cars c
JOIN car_groups g
  ON c.engine_displacement = g.engine_displacement
  AND c.horsepower = g.horsepower
  AND c.power = g.power;

-- Step 3: aggregazioni per ogni gruppo
INSERT OVERWRITE DIRECTORY '/user/frompoo/data/output_job3_Hive'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT
  group_id,
  ROUND(AVG(price), 2) AS avg_price,
  MAX(horsepower) AS max_hp,
  CONCAT_WS(',', COLLECT_SET(model_name)) AS models
FROM cars_with_group
GROUP BY group_id;
