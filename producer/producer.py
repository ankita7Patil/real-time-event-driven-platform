from kafka import KafkaProducer
import json
import time
import uuid
from datetime import datetime
import random

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "order-events"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

ORDER_STATUSES = ["PLACED", "CONFIRMED", "SHIPPED", "DELIVERED"]
SOURCES = ["WEB", "MOBILE", "API"]

def generate_order_event():
    return {
        "event_type": "ORDER_EVENT",
        "order_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(100, 999)}",
        "status": random.choice(ORDER_STATUSES),
        "timestamp": datetime.utcnow().isoformat(),
        "source": random.choice(SOURCES)
    }

if __name__ == "__main__":
    print("🚀 Order Event Producer started...")

    while True:
        event = generate_order_event()
        producer.send(TOPIC_NAME, event)
        producer.flush()
        print("📤 Sent event:", event)
        time.sleep(2)
