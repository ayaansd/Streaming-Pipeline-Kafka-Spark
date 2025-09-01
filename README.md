
# Streaming Pipeline — Kafka + Spark Structured Streaming

**Goal:** Process job-event streams in real-time, detect anomalies, and publish aggregates for dashboards.

## Local Mock (no Kafka required)
```bash
python stream_mock.py
```

## With Kafka (outline)
- Producer writes JSON to topic `job_events`.
- Spark reads from Kafka, aggregates per minute, flags anomalies.
- Sink to console / parquet / REST endpoint.
