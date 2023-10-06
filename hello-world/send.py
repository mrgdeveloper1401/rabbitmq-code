# #!/usr/bin/env python
# import pika

# # create a connection
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# # create a channel
# ch1 = connection.channel()
# # create a queue
# ch1.queue_declare(queue='hello')

# # create a basic_publish
# # create a notification channel
# ch1.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# print('message sent!')




#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()