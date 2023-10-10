import pika

# create a connection or server connection
conncetion = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create a channel
channel = conncetion.channel()

# create a queue
channel.queue_declare(queue='hello')

# create a basic_publish
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='hello world!'
)
print('Sent hello world!')

# close the connection
conncetion.close()