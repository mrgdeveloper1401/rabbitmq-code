import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()
channals.exchange_declare(exchange='direct_logs', exchange_type='direct')

resualt = channals.queue_declare(queue='', durable=True)
qname = resualt.method.queue

serverities = ('info', 'warning', 'error')


for serverity in serverities:
    channals.queue_bind(exchange='direct_logs', queue=qname, routing_key=serverity)
    
print('waiting for message')

def callback(ch, method, properties, body):
    print(f'received {body}')
channals.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)