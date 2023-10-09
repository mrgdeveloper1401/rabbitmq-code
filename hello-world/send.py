import pika

# create a connection
conncetion = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create a channel
channel = conncetion.channel()

# create a queue
channel.queue_declare(queue='hello-world')

# create a basic_publish
channel.basic_publish(
    exchange='',
    routing_key='hello-world',
    body='hello world!'
)
print('Sent hello world!')

# close the connection
conncetion.close()