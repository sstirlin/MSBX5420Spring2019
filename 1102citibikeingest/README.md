# CitiBike data ingestion

Write a python script (NOT a Jupyter notebook) that polls the CitiBike endpoint
every 10 seconds and ingests the station update.  Each station update should then
be written to a kafka topic named `citibike.station.update.1`.
