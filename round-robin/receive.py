import pika
import time
import sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channals = connection.channel()

    channals.queue_declare(queue='first', durable=True)

    print('wating for message press ctrl+c to exit')

    def callback(channals, method, properties, body):
        print(f'Received {body}')
        print(properties.headers)
        time.sleep(9)
        print('done')
        channals.basic_ack(delivery_tag=method.delivery_tag)
        
    channals.basic_qos(prefetch_count=1)
    channals.basic_consume(queue='first', on_message_callback=callback, auto_ack=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)