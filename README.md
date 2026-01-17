\# Real-Time Event-Driven Order Processing Platform



\## 📌 Overview

This project is a \*\*real-time event-driven system\*\* built using \*\*Apache Kafka, Docker, and Python\*\*.

It simulates how large-scale systems like \*\*Uber, Amazon, Swiggy, and Instagram\*\* process events such as

orders, status updates, notifications, and analytics in real time.



The goal of this project is to demonstrate \*\*Kafka producers, multiple consumer services,

consumer groups, and real-time data streaming\*\* using an industry-style architecture.



---



\## 🏗️ System Architecture



Producer ➜ Kafka Topic ➜ Multiple Consumer Services



\### Components:

\- \*\*Producer Service\*\*

&nbsp; - Generates structured order events

&nbsp; - Publishes events to Kafka topic



\- \*\*Kafka\*\*

&nbsp; - Acts as the real-time event streaming backbone

&nbsp; - Decouples producers and consumers



\- \*\*Consumer Services\*\*

&nbsp; - Order Processing Service

&nbsp; - Analytics Service

&nbsp; - Storage (Persistence) Service



Each consumer runs in a \*\*separate consumer group\*\*, allowing independent and scalable processing.



---



\## 🔄 Event Flow



1\. Producer generates an `OrderEvent`

2\. Event is published to Kafka topic `order-events`

3\. Multiple consumers read the same event independently

4\. Events are processed, analyzed, and stored in real time



---



\## 🧩 Event Schema (OrderEvent)



```json

{

&nbsp; "event\_type": "ORDER\_EVENT",

&nbsp; "order\_id": "uuid",

&nbsp; "user\_id": "user\_123",

&nbsp; "status": "PLACED | CONFIRMED | SHIPPED | DELIVERED",

&nbsp; "timestamp": "ISO-8601 datetime",

&nbsp; "source": "WEB | MOBILE | API"

}



