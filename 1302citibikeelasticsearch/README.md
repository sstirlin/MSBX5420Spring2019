# Ingestion of CitiBike data into Elasticsearch

In this homework we will pull together the pieces that we have been learning
over the past few weeks.

In Week 11 we built a script that scrapes the CitiBike website and ingests
the data into a Kafka topic.  Open up a terminal and start this script.  This
will start filling the Kafka topic with data (people say "hydrate" with data, even
though I abhor this terminology).

## Part 1

Build a python script (not a notebook) that consumes from the kafka topic
and enriches (or "annotates") each message.  We will call this script
`citibike_annotator.py`.  You will submit this to Canvas (however, wait until
Part 2 below to do so since we will add to it).

Recall that each message is in json format and looks like this:
```
{"station_id":"72",
 "num_bikes_available":16,
 "num_ebikes_available":0,
 "num_bikes_disabled":6,
 "num_docks_available":33,
 "num_docks_disabled":0,
 "is_installed":1,
 "is_renting":1,
 "is_returning":1,
 "last_reported":1555275625,
 "eightd_has_available_keys":false}
```

We want to enrich this data using the "station information" data available at the URL

https://gbfs.citibikenyc.com/gbfs/en/station_information.json

Since station information doesn't update very often, for the purposes of this assignment
you can treat it as static.  In other words, just scrape the station information once when
your script starts (in the real world we might re-scrape this endpoint once per week perhaps).

Each station information record looks like this:
```
{"station_id":"72",
 "external_id":"66db237e-0aca-11e7-82f6-3863bb44ef7c",
 "name":"W 52 St & 11 Ave",
 "short_name":"6926.01",
 "lat":40.76727216,
 "lon":-73.99392888,
 "region_id":71,
 "rental_methods":["KEY","CREDITCARD"],
 "capacity":55,
 "rental_url":"http://app.citibikenyc.com/S6Lr/IBV092JufD?station_id=72",
 "electric_bike_surcharge_waiver":false,
 "eightd_has_key_dispenser":false,
 "has_kiosk":true}
```

So let's "enrich" your station update with this relevant information (this is basically a table join).  Your
script should emit a message that looks like this:
```
{"station_id":"72",
 "num_bikes_available":16,
 "num_ebikes_available":0,
 "num_bikes_disabled":6,
 "num_docks_available":33,
 "num_docks_disabled":0,
 "is_installed":1,
 "is_renting":1,
 "is_returning":1,
 "last_reported":1555275625,
 "eightd_has_available_keys":false,
 "external_id":"66db237e-0aca-11e7-82f6-3863bb44ef7c",
 "name":"W 52 St & 11 Ave",
 "short_name":"6926.01",
 "lat":40.76727216,
 "lon":-73.99392888,
 "region_id":71,
 "rental_methods":["KEY","CREDITCARD"],
 "capacity":55,
 "rental_url":"http://app.citibikenyc.com/S6Lr/IBV092JufD?station_id=72",
 "electric_bike_surcharge_waiver":false,
 "eightd_has_key_dispenser":false,
 "has_kiosk":true}
```

For now just make sure that your script *prints* out each message.  In Part 2 we'll push these into Elasticsearch.
Note that I just wholesale grabbed every field from station_information.  In the real world I might be more selective
since this bloats the size of each message (and hence costs $$$).


## Part 2
