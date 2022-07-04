from base64 import encode
import json
import time
import kafka
from kafka import KafkaProducer
import datetime
from utils import *
import math

Kafka_topic = "orders_list"
Order_limit = 150000

producer = KafkaProducer(bootstrap_servers="0.0.0.0:29092")


Sattus_list=['Shipped','Removed_From_Basket','Basket_Not_Paid','Rejected_after_shipment']
start_date = datetime.datetime.strptime('6/1/2022 1:30 AM', '%m/%d/%Y %I:%M %p')
end_date = datetime.datetime.strptime('7/1/2022 4:50 AM', '%m/%d/%Y %I:%M %p')
Istanbul = {"latitude":41.015137,"longitude":28.979530}
order_items =['Iphone','Book','Ipad','MacBook','Coffee','Milk','Grape']

for i in range(1, Order_limit):
    t = randomGeo(Istanbul,10000)
    data = {
       "order_number": i+100000,
       "quantity_order": random.randint(1,22),
       "price_each":random.randint(30,6000),
       "order_date": str(random_date(start_date, end_date)),
       "status": random.sample(Sattus_list,1)[0] ,
       "user_id": f"tom_{i}",
       "latitude":t['latitude'],
       "longitude":t['longitude'],
       "items": random.sample(order_items,1)[0],
    }
    
    producer.send(Kafka_topic, json.dumps(data).encode("utf-8"))
    print(f"Sending...order number{i}")
