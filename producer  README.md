# Kafka Transaction Producer

This module will contain the Python producer responsible for reading historical transaction data and publishing transactions continuously to an Apache Kafka topic.

## Planned Workflow

PaySim Dataset
      ↓
Python Producer
      ↓
Kafka Topic
      ↓
Spark Structured Streaming
