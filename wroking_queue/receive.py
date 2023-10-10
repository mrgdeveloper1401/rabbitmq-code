import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='working_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(channel, method, properties, body):
    # print(f" [x] Received {body.decode()}")
    print(f'received {body}')
    print(properties.headers)
    # time.sleep(body.count(b'.'))
    print(" [x] Done")
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(method)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='working_queue', on_message_callback=callback)

channel.start_consuming()