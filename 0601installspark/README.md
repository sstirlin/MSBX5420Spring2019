BEFORE PROCEEDING:  Go back to Week 5 lecture and cover the last bit about Grouping in Spark!!!


# Install HDFS and Spark cluster

We are done with the `jupyter/all-spark-notebook` docker container.  This
has been a useful "one-stop shop" (everything bundled into a single docker container),
but we want to dig more into the internals of Spark.

In the VM stop the container:
```
docker stop spark
```

We also had previousy downloaded an HDFS docker image, but we never used it.
In fact there's a better way to run HDFS, so let's just delete this image:
```
docker rmi sequenceiq/hadoop-docker:2.7.1
```


## Install HDFS and Spark cluster

We're going to run proper HDFS and Spark clusters (using docker).  Even though
these will still be running on your laptop, they look and behave like real (albeit low-horsepower)
HDFS and Spark clusters.

I have created a cluster configuration that will make this whole thing
easy.  Start by downloading my cluster configuration:
```
cd ~/work
git clone https://github.com/sstirlin/docker-spark.git
cd docker-spark
```

In this directory you will see a file named `docker-compose.yml`.

If you are curious, go ahead and open it up in `nano`.  Basically, this file
describes how to launch (and knit together) several docker containers that make up our
Spark and HDFS clusters.  We will discuss this more in class.

Think of this file as replacing a bunch of individual `docker run ...` commands.
We will use a helpful command called `docker-compose` to manage our little mini
clusters for us.

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
The last command configures the DNS so we can refer to our containers by name
instead of IP address.  I'll discuss this in class.

We're going to use Anaconda Python (like in Week 2) to talk to
our HDFS and Spark clusters.  First, activate your Python environment
(this was installed in Week 2):
```
conda activate py37
```

Let's install some packages in order to talk to Spark and HDFS:
```
conda install pyspark=2.4.0 python-hdfs
```

Now just start Jupyter:
```
jupyter notebook
```

I will demonstrate in lecture how to connect to both HDFS and Spark from Jupyter, but if
you are curious then you can check out [this example Jupyter notebook](hello_world_spark.ipynb).

When you are done with the HDFS and Spark clusters you can shut them down with the following
commands:
```
cd ~/work/docker-spark/
docker-compose down
```
