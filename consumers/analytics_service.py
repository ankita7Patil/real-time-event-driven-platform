from kafka import KafkaConsumer
import json
from collections import Counter

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "order-events"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="analytics-group",
    auto_offset_reset="earliest"
)

print("📊 Analytics Service started...")

status_counter = Counter()

for message in consumer:
    event = message.value
    status = event["status"]
    status_counter[status] += 1

    print("📊 Order Status Metrics:", dict(status_counter))
