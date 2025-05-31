# Command to run for setting up the entire environment 

source venv/bin/activate
pip install kaggle pandas

if [ -z "$ROOT_DIR" ]; then
    export ROOT_DIR=$(pwd)
fi

$HADOOP_HOME/bin/hdfs namenode -format
$HADOOP_HOME/sbin/start-dfs.sh

# Download Dataset
cd data
kaggle datasets download -d ananaymital/us-used-cars-dataset
unzip us-used-cars-dataset.zip
rm us-used-cars-dataset.zip
cd ..

# Dataset Cleaning
python scripts/database_cleaner.py
cd data
rm used_cars_data.csv

# Uploading of the cleaned dataset on HDFS
hdfs dfs -mkdir -p /user/$USER/data
hdfs dfs -put vehicles_clean.csv /user/$USER/data

# Stopping HDFS and venv
$HADOOP_HOME/sbin/stop-dfs.sh
deactivate