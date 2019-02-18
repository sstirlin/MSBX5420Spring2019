# Introduction to HDFS

## Uploading files into HDFS tutorial

Start the cluster
```
cd ~/work/docker-spark
docker-compose up -d
bash expose_hostnames.sh
```

Start Jupyter
```
cd ~/work/week6
conda activate py37
jupyter notebook
```

Now follow [this notebook](lecture_uploadhdfs.ipynb).

When finished with the cluster you can bring it down like this:
```
cd ~/work/docker-spark
docker-compose down
```
