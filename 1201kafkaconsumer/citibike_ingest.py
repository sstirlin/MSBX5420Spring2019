import time
import requests
from retrying import retry
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer
from concurrent.futures import wait
import ujson


station_status_topic = 'citibike.station.status.1'
station_status_url = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
brokers = 'kafka-1:9092'

admin = AdminClient({'bootstrap.servers': brokers})


def delete_station_status_topic():
    """Deletes the station status topic if it exists
    """
    topics = admin.list_topics(timeout=10).topics.keys()

    # delete topic if exists 
    while station_status_topic in topics:
        print("Trying to delete " + station_status_topic)
        status = admin.delete_topics([station_status_topic])
        fut = status[station_status_topic]
        try:
            fut.result()
        except Exception as e:
            print(e)
        topics = admin.list_topics(timeout=10).topics.keys()


def create_station_status_topic():
    """Creates the station status topic if it doesn't already exist
    """
    topics = admin.list_topics(timeout=10).topics.keys()

    # create topic if doesn't already exist
    while station_status_topic not in topics:
        print("Trying to create " + station_status_topic)
        status = admin.create_topics([NewTopic(station_status_topic, num_partitions=3, replication_factor=1)])
        fut = status[station_status_topic]
        try:
            fut.result()
        except Exception as e:
            print(e)
        topics = admin.list_topics(timeout=10).topics.keys()

    print(topics)


@retry(wait_exponential_multiplier=1000)
def scrape_station_status():
    """Scrapes station status from Citibike, with retry logic if fails
    """
    r = requests.get(station_status_url)
    if r.status_code != 200:
        raise IOError("Station status fetch failed!")
    return r.json()


if __name__ == '__main__':

    delete_station_status_topic()
    create_station_status_topic()

    p = Producer({'bootstrap.servers': 'kafka-1:9092'})
    
    while True:
        data = scrape_station_status()
        for msg in data['data']['stations']:
            msgbytes = ujson.dumps(msg).encode('utf-8')
            print(msgbytes)
            p.produce(station_status_topic, msgbytes) 

        p.flush()
        print("Done flushing")
        time.sleep(10)

    #p.flush()
