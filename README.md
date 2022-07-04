# Kafka_Stream_Python

This project is to simulate recommendation engine on stream data. 

1. we need to install zookeeper and kafka , use the following command :

```
docker-compose -f docker-compose3.yml up  -d
```
2. order_producer.py will produce orders messages in order topic in kafka :) some sample data should look like:

```

{'order_number': 249992, 'quantity_order': 10, 'price_each': 2356, 'order_date': '2022-06-10 10:42:10', 'status': 'Rejected_after_shipment', 'user_id': 'tom_149992', 'latitude': 41.03910960386379, 'longitude': 28.982571408811562, 'items': 'Book'}

{'order_number': 249993, 'quantity_order': 2, 'price_each': 2557, 'order_date': '2022-06-24 08:26:24', 'status': 'Removed_From_Basket', 'user_id': 'tom_149993', 'latitude': 40.988245703085404, 'longitude': 28.91988232566403, 'items': 'Iphone'}

```

3. we need to geoHASH the locations
