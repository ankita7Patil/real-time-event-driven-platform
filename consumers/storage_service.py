from kafka import KafkaConsumer
import json

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "order-events"
OUTPUT_FILE = "stored_events.jsonl"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="storage-group",
    auto_offset_reset="earliest"
)

print("💾 Storage Service started...")

with open(OUTPUT_FILE, "a") as file:
    for message in consumer:
        event = message.value
        file.write(json.dumps(event) + "\n")
        file.flush()
        print("💾 Event stored:", event["order_id"])
