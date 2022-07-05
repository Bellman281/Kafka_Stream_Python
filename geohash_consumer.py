import geohash

import json

from kafka import KafkaConsumer


Kafka_topic = "orders_list"


consumer = KafkaConsumer(Kafka_topic,bootstrap_servers="0.0.0.0:29092")

total_orders_count = 0
total_revenue = 0
print("GEOHASH is listening")
while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        latitude = float(consumed_message["latitude"])
        longitude = float(consumed_message["longitude"])
        geohash_9 =geohash.encode(latitude,longitude, precision=9)
        geohash_8 =geohash.encode(latitude,longitude, precision=8)
        geohash_7 =geohash.encode(latitude,longitude, precision=7)
        geohash_6 =geohash.encode(latitude,longitude, precision=6)
        user_id = consumed_message['user_id']
        print(f"GeoHASH for : {user_id}")
        print(f"GEO HASH percision 9: {geohash_9}")
        print(f"GEO HASH percision 8: {geohash_8}")
        print(f"GEO HASH percision 7: {geohash_7}")
        print(f"GEO HASH percision 6: {geohash_6}")
