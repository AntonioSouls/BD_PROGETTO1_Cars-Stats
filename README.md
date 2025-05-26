# <div align="center"> CARS STATS </div>
The following project is the first of two delivered during the Big Data course. The aim of this project is to learn how to use and put into practice technologies such as Hadoop, Hive and Spark on a real case study. This repository shows the implementation that my colleague [Matteo Vitale](https://github.com/MatVitale6) and [I](https://github.com/AntonioSouls) decided to apply to solve the specifications required by the project. In particular, out of all the project specifications (below), we chose to implement the `first` and `third` as we felt they were the most interesting to work on and the ones that were really most applicable in a real context.

## Project Specifications
Consider the US Used Cars Dataset from Kaggle, which contains about 3 million records with detailed 
information about used cars for sale up to 2020. The dataset is in CSV format, and each record includes 66 
columns listed on the next page. 
After properly preparing the dataset (e.g., by removing incorrect or non-significant data), design and implement 
at least two of the following analyses using at least three of the following technologies: `MapReduce`, `Hive`, `Spark Core` and `Spark SQL`: 
1. A job that generates statistics for each car brand (make_name) in the dataset, indicating, for each brand:
    - The brand name; 
    - A list of models (model_name) for that brand including;
    - For each model: 
        - The number of cars in the dataset;
        - The minimum, maximum, and average price (price) of that model in the dataset;
        - The list of years in which the model appears in the dataset; 
2. A job that produces a report for each city and year showing:
    - The number of car models for sale in that year belonging to three price ranges (high: over $50K, medium: between $20K and $50K, low: below $20K);
    - For each range, also report: 
        - The number of cars in that range;
        - The average number of days on the market (daysonmarket);
        - The three most frequent words appearing in the car descriptions (description). 
3. A job that groups car models with “similar” engine characteristics—i.e., models whose horsepower and 
engine displacement values differ by at most 10%. For each group, report the average price and the model with the highest horsepower.

## Description of our Work

## Authors
<a href="https://github.com/AntonioSouls">
  <img src="https://github.com/AntonioSouls.png" width="80">
</a>
<a href="https://github.com/MatVitale6">
  <img src="https://github.com/MatVitale6.png" width="80">
</a>

