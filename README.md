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

## How to use this Software
To be able to use our solution, it is important to carry out the following steps:
### Environment Setup
- Install Hadoop, Hive & Spark
- Create Kaggle Account: https://www.kaggle.com/
- Go to "My Account" > "Create API Token"
- Download file kaggle.json
- Move it into ~/.kaggle/ folder:
  ```bash
  mv ~/Downloads/kaggle.json ~/.kaggle/
  ```
- Cloning the repository locally:
  ```bash
  git clone https://github.com/AntonioSouls/BD_PROGETTO1_Cars-Stats.git
  ```
- Create local folders:
  ```bash
  mkdir -p ~/<YOUR-PATH-TO-PROJECT>/BD_PROGETTO1_Cars-Stats/data
  cd ~/<YOUR-PATH-TO-PROJECT>/BD_PROGETTO1_Cars-Stats
  ```
- Initialise and Activate the virtual environment:
  ```bash
  python3 -m venv venv
  ```
- Starting the automatic setup
  ```bash
  bash setup.sh
  ```
These listed are the commands to be executed only at the first execution of the project because are useful commands for setting the working environment, downloading the dataset and cleaning it all automatically
### Execution after the setup
The following is the command to start the project. (If it is not the first execution of the project, you can start directly from the following):
- ```bash
  bash start.sh
  ```

## Authors
<a href="https://github.com/AntonioSouls">
  <img src="https://github.com/AntonioSouls.png" width="80">
</a>
<a href="https://github.com/MatVitale6">
  <img src="https://github.com/MatVitale6.png" width="80">
</a>

## Sezione Temporanea con gli step da svolgere
- Scaricare il Dataset [(Io)](https://github.com/AntonioSouls);✅
- Creare uno script per pulirlo [(Io)](https://github.com/AntonioSouls);✅
- Creare un bash per automatizzare i due step precedenti [(Io)](https://github.com/AntonioSouls);✅
- Creare due script per risolvere i job con MapReduce [(Io)](https://github.com/AntonioSouls);
- Creare due script per risolvere i job con Hive [(Io)](https://github.com/AntonioSouls);
- Creare due script per risolvere i job con Spark [(Matteo)](https://github.com/MatVitale6);
- Creare una sorta di interfaccia per poter selezionare quale job eseguire e con quale tecnologia [(Matteo)](https://github.com/MatVitale6);

