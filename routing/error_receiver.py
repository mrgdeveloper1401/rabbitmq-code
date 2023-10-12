import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()
channals.exchange_declare(exchange='direct_logs', exchange_type='direct', durable=True)

resualt = channals.queue_declare(queue='', durable=True)
qname = resualt.method.queue

serverities = 'error'

channals.queue_bind(exchange='direct_logs', queue=qname, routing_key=serverities)

print('waiting for message')

def callback(channals, method, properties, body):
    with open('error_logs.log', 'a') as f:
        f.write(str(f'{body}\n'))
channals.basic_consume(queue=qname, on_message_callback=callback, auto_ack=False)
channals.start_consuming()