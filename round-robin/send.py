import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channals = connection.channel()


channals.queue_declare(queue='first', durable=True)

message = 'this is a test message'

channals.basic_publish(exchange='',
                      routing_key='first',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2, headers={'name': 'mohammad goodarzi'}))

print('sent message')

connection.close()