from confluent_kafka import Consumer, KafkaException

# Configura el Consumer para conectarse a los brokers
consumer_conf = {
    'bootstrap.servers': 'localhost:9093,localhost:9095,localhost:9097',
    'group.id': 'mi-grupo-consumidor',
    'auto.offset.reset': 'earliest'  # Empieza desde el principio si no hay un offset guardado
}
consumer = Consumer(consumer_conf)

# Suscribirse al tópico "mi-topico"
consumer.subscribe(['mi-topico'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Espera 1 segundo por mensajes
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        print(f"Mensaje recibido: key={msg.key().decode('utf-8')}, value={msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    print("Consumo interrumpido")

finally:
    # Cerrar el consumidor de forma segura
    consumer.close()
