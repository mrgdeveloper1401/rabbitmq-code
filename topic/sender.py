import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()

channals.exchange_declare(exchange='topic', exchange_type='topic', durable=True)

messages = {
    'error.wrning.important': 'this is an important message',
    'info.debug.notimportant': 'this is an not an important message',
}

for key, value in messages.items():
    channals.basic_publish(exchange='topic', routing_key=key, body=value)

print('sent messages')
connection.close()