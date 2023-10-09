import pika, os, sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    
    channel.queue_declare(queue='hello-world')
    
    def callback(channel, method, properties, body):
        print(f'received {body}')
        
    channel.basic_consume(
        queue='hello-world',
        on_message_callback=callback,
        auto_ack=True
    )
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)