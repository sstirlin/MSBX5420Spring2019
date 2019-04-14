## How to install your Elasticsearch cluster

If you are running any other docker containers now, please shut them down.

This Elasticsearch cluster also contains its own Kafka cluster (which is just the same as the
Kafka cluster that you already have).  However, you need to shut down your other Kafka cluster
(otherwise you'll be running two instances and causing chaos).
```
cd ~/work
git clone https://github.com/sstirlin/docker-elasticsearch
cd docker-elasticsearch

docker-compose pull
```


## How to bring up your Elasticsearch cluster

```
cd ~/work/docker-elasticsearch
docker-compose up -d
bash expose_hostnames.sh

conda activate py37
cd ~/work
mkdir week13
cd week13
jupyter notebook
```


## How to shut down your Elasticsearch cluster

```
cd ~/work/docker-elasticsearch
docker-compose down
```

## Lecture materials

Slides here:

https://docs.google.com/presentation/d/1wg3O8UDExdbrRPzBYHuTvPJX2i3l0z_ZN90iP3LpbMA/edit?usp=sharing

How to hit Elasticsearch's REST API in this [notebook](elasticsearch_rest.ipynb)
