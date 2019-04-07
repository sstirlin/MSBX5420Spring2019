# CitiBike data ingestion

Write a python script (NOT a Jupyter notebook) that polls the CitiBike endpoint
every 10 seconds and ingests the station updates.

Note that each time you poll CitiBike you will receive a single big json message
that contains the updates for ALL stations.  You should break this up (one message
per station) and write each message to a kafka topic named `citibike.station.update.1`.

A very useful command-line utility is called `kafkacat`.  You can install it like this:
```
sudo apt-get install kafkacat
```
This utility acts as a consumer (or you can write you own consumer in Python like we
did in lecture).  `kafkacat` makes it easy to just double-check that there are messages
in a topic.  You run it like this:
```
kafkacat -b kafka-1:9092 -o beginning -t citibike.station.update.1
```
