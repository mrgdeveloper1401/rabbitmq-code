import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()

channals.exchange_declare(exchange='topic_logs', exchange_type='topic')

results = channals.queue_declare(queue='', exclusive=True)
queue = results.method.queue

binding_keys = '#.notimportant'
channals.queue_bind(exchange='topic_logs', queue=queue, routing_key=binding_keys)

def callback(ch, method, properties, body):
    print(f'{body}')
channals.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)