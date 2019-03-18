Slides here:

https://docs.google.com/presentation/d/1AiMKgkFS1WGAIYXYAXHQJgAkTmoL6yr1TW42rOg0bhQ/edit?usp=sharing


## How to install your Kafka cluster

```
cd ~/work
git clone https://github.com/sstirlin/docker-kafka
cd docker-kafka

docker-compose pull

# install the python client library so that we can talk to Kafka
conda activate py37
pip install confluent-kafka
```


## How to bring up your Kafka cluster

```
cd ~/work/docker-kafka
docker-compose up -d
bash expose_hostnames.sh

cd ~/work
mkdir week10
cd week10
jupyter notebook
```


## How to shut down your Kafka cluster

```
cd ~/work/docker-kafka
docker-compose down
```
