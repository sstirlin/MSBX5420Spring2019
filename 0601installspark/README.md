# Install HDFS and Spark cluster

We are done with our trusty `jupyter/all-spark-notebook` docker container.  This
has been a useful "one-stop shop" and we've learned a lot from it, but it is time
to say goodbye.

In the VM stop and remove the container:
```
docker stop spark
docker rm spark
```

We also had previousy downloaded an HDFS docker image, but we never used it.
In fact there's a better way to run HDFS, so let's just delete this image:
```
docker rmi sequenceiq/hadoop-docker:2.7.1
```

Sorry about the confusion there.


## Install HDFS and Spark cluster

We're going to run proper HDFS and Spark clusters using docker because
it is instructive to see the details of how the clusters are configured.

In the VM start by downloading a cluster configuration file:
```
cd ~/work
git clone https://github.com/sstirlin/docker-spark.git
cd docker-spark
```

Inside of here you will see a file named `docker-compose.yml`.  You are
welcome to open it up in `nano` and have a look.  Basically, this file
describes how to stand up a "real" Spark cluster (complete with a dedicated
master node and a single worker node) and a "real" HDFS
cluster (complete with a dedicated namenode and a single datanode).

We could easily add more Spark worker nodes and more HDFS datanodes, but
the VM will be unhappy so let's not.

When managing multiple docker containers as a cluster, the `docker-compose`
command is extremely useful.  Rather than running individual `docker run ...`
commands for each container, you can just create a `docker-compose.yml` configuration
file and let `docker-compose` do all of the hard work for you.

For now let's just pull down all the containers that we need:
```
docker-compose pull
```
This command could take hours.


## Run Jupyter, Spark, and HDFS

After installation let's bring up the Spark and HDFS clusters:
```
cd ~/work/docker-spark
docker-compose up -d
bash expose_hostnames.sh
```
The last script is some magic to configure the DNS so that
we can talk to our containers by *name* (instead of IP address).

We're going to use Anaconda Python (like we used in Week 2) to talk to
our HDFS and Spark clusters.  First, activate your Python environment
(this was installed in Week 2):
```
conda activate py37
```

Let's install some packages in order to talk to Spark and HDFS:
```
conda install pyspark python-hdfs
```

Now just start Jupyter:
```
jupyter notebook
```

I will demonstrate in lecture how to connect to both HDFS and Spark from Jupyter, but if
you are curious then you can check out [this example Jupyter notebook](hello_world_spark.ipynb).

When you are done with the HDFS and Spark clusters you can shut them down by entering the following
into a terminal (inside your Linux VM):
```
cd ~/work/docker-spark/
docker-compose down
```
