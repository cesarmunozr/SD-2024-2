from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({
    'bootstrap.servers': 'localhost:9093,localhost:9095,localhost:9097'
})

new_topic = NewTopic("mi-topico", num_partitions=3, replication_factor=3)
topic_list = [new_topic]

fs = admin_client.create_topics(topic_list)

for topic, f in fs.items():
    try:
        f.result()  # Bloquea hasta que se complete la creación del tópico
        print(f"Tópico {topic} creado exitosamente")
    except Exception as e:
        print(f"Fallo al crear el tópico {topic}: {e}")
