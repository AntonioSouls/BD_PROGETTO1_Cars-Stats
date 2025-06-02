# Command to run for starting the virtual environment and HDFS automatically

source venv/bin/activate
rm -rf /tmp/*
$HADOOP_HOME/bin/hdfs namenode -format
$HADOOP_HOME/sbin/start-dfs.sh
cd data
hdfs dfs -mkdir -p /user/$USER/data
hdfs dfs -put vehicles_clean.csv /user/$USER/data