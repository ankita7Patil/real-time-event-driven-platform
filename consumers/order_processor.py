from kafka import KafkaConsumer
import json

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "order-events"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="order-processing-group",
    auto_offset_reset="earliest"
)

print("📦 Order Processing Service started...")

for message in consumer:
    event = message.value
    print(f"📦 Processing Order {event['order_id']} | Status: {event['status']}")
