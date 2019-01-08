Work in progress...


## Quickstart to get HDFS and Spark running

Start the VM and run the following commands inside it (in a terminal)
```sh
# Activate your python environment
conda activate py37

# Let's install some packages (should only need to run this once)
conda install pyspark python-hdfs

# Download the docker-spark repo from github (should only need to run this once)
cd ~/projects
git clone https://github.com/sstirlin/docker-spark.git

# start the docker containers (running this the first time requires downloading about 2GB... could take hours)
cd docker-spark
docker-compose up -d
bash expose_hostnames.sh

# Now let's start Jupyter
jupyter notebook

# A browser should open up in your VM now.  You are in Jupyter NOW!!!
# Click New->Python 3 to start a new Python 3 notebook.

```

Check out [this example Jupyter notebook](hello_world_spark.ipynb) that shows how to use this
HDFS and Spark cluster. 

Inside of Jupyter you can run the following commands
