Steps :-

1)  Start zookeeper server from KAFKA_HOME 
    
    
    command - 
    nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zk.log & 
      
2) Start kafka server from KAFKA_HOME 

    
    command - 
    nohup bin/kafka-server-start.sh config/server.properties > kb.log &
    

Note : 
By default kafkaProducer.py will create the topic with partition as 1 and replication factor as 1 in case if it is not existing and push messages to it.


    
     

