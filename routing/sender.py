import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()

channals.exchange_declare(exchange='direct_logs', exchange_type='direct')

messages = {
    'info': 'this is an info message',
    'error': 'this is an error message',
    'warning': 'this is a warning message',
}

for key, value in messages.items():
    channals.basic_publish(exchange='direct_logs', routing_key=key, body=value)
    
connection.close()