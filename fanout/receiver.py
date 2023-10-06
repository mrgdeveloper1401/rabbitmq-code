import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channals = connection.channel()

    channals.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)
    resualt = channals.queue_declare(queue='', exclusive=True)
    qname = resualt.method.queue
    channals.queue_bind(exchange='logs', queue=qname, routing_key='')
    print('waiting for logs')
    
    def callback(channals, method, properties, body):
        print(f'received message {body}')
    
    channals.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
    channals.start_consuming()