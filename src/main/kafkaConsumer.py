# Before starting the producer/consumer, start zookeeper server and then kafka server

from kafka import KafkaConsumer

consumer = KafkaConsumer(enable_auto_commit=True,auto_commit_interval_ms=10)
consumer.subscribe("two")
for i in consumer :
    print(i)
    consumer.commit_async(offsets=10)