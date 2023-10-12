import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()
channals.exchange_declare(exchange='direct_logs', exchange_type='direct', durable=True)

resualt = channals.queue_declare(queue='', durable=True, exclusive=True)
qname = resualt.method.queue

serverities = ('info', 'error', 'warning')


for serverity in serverities:
    channals.queue_bind(exchange='direct_logs', queue=qname, routing_key=serverity)
    
print('waiting for message')

def callback(ch, method, properties, body):
    print(f'{method.routing_key}, received {body}')
channals.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
channals.start_consuming()