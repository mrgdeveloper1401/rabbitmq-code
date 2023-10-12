import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='fanouts', exchange_type='fanout', durable=True)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='fanouts', queue=queue_name)

print(' [*] Waiting for fanouts. To exit press CTRL+C')

def callback(channel, method, properties, body):
    print(f" [x] {body}")
    print(queue_name)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()