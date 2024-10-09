from confluent_kafka import Producer
import time

# Configura el Producer para conectarse a los brokers
producer_conf = {
    'bootstrap.servers': 'localhost:9093,localhost:9095,localhost:9097'
}
producer = Producer(producer_conf)

# Callback para confirmar la entrega del mensaje
def delivery_report(err, msg):
    if err is not None:
        print(f"Error al entregar mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}]")

# Produce 10 mensajes al tópico "mi-topico"
for i in range(10):
    message = f"Mensaje {i}"
    producer.produce('mi-topico', key=str(i), value=message, callback=delivery_report)
    time.sleep(1)  # Simula un retraso entre envíos
    producer.poll(0)  # Llama para manejar los reportes de entrega

# Espera a que todos los mensajes pendientes sean entregados
producer.flush()
