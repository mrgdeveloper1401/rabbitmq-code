import pika
import uuid

class Vpn:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channals = self.connection.channel()
        result = self.channals.queue_declare(queue='', exclusive=True) 
        self.queue_name = result.method.queue
        self.channals.basic_consume(queue=self.queue_name, on_message_callback=self.on_response, auto_ack=True)
        
    def on_response(self, channals, method, properties, body):
        if self.core_id == properties.corerelation_id:
            self.responce = body
        
    # create method and send information to server
    def call(self, number):
        self.responce = None
        self.core_id = str(uuid.uuid4())
        send.channals.basic_publish(exchange='', routing_key='rpc_queue',
        properties=pika.BasicProperties(reply_to=self.queue_name, correlation_id=self.core_id,
        body=str(number)))
        while self.responce is None:
            self.connection.process_data_events()
        return int(self.responce)

send = Vpn()
responce = send.call(30)
print(responce)