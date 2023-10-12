import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()

channals.exchange_declare(exchange='topic_logs', exchange_type='topic', durable=True)

results = channals.queue_declare(queue='', exclusive=True, durable=True)
queue_name = results.method.queue

binding_keys = '#.notimportant'
channals.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_keys)

print('wating message')

def callback(channals, method, properties, body):
    print(f'{body}')
channals.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channals.start_consuming()