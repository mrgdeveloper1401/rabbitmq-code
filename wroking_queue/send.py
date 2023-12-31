#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='working_queue', durable=True)

# message = ' '.join(sys.argv[1:]) or "Hello World!"
message = 'this test message'
channel.basic_publish(
    exchange='',
    routing_key='working_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,
        headers={'name': 'mohammad',
        'age': 20}
    ))
print(f"Sent {message}")
connection.close()