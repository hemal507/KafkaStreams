# Before starting the producer/consumer, start zookeeper server and then kafka server

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',acks="all",linger_ms=100,batch_size=100)
for i in range(30) :
    producer.send("three", key='Key'+str(i), value="welcome to python kafka stream "+str(i) )
producer.flush()
metrics = producer.metrics()
print(metrics)
