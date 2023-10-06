import pika



connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()


channals.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)

def callback(channals, method, properties, body):
    pass
channals.basic_publish(exchange='logs', routing_key='logs', body='this is a test message')
print('send message')
connection.close()