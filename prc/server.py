import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channals = connection.channel()
channals.queue_declare(queue='rpc_qeue', exclusive=True)

def callback(channals, method, properties, body):
    number = int(body)
    print('processign message')
    response = number + 1
    channals.basic_publish(exchange='', routing_key=properties.reply_to,
        properties=pika.BasicProperties(correlation_id=properties.correlation_id),
        body=str(response))
    channals.basic_ack(delivery_tag=method.delivery_tag)


channals.basic_qos(prefetch_count=1)
channals.basic_consume(queue='rpc_qeue', on_message_callback=callback)
print('waiting for messages')
channals.start_consuming()