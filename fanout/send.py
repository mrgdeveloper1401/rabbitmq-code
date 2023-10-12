import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)

message = 'info hello worlds'
channel.basic_publish(exchange='fanouts', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()