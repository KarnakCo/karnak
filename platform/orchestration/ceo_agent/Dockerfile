FROM python:3.11-slim
WORKDIR /app
COPY platform/common /app/platform/common
COPY platform/orchestration/ceo_agent /app/platform/orchestration/ceo_agent
RUN pip install --no-cache-dir nats-py kafka-python prometheus-client opentelemetry-sdk opentelemetry-exporter-otlp
CMD ["python", "/app/platform/orchestration/ceo_agent/main.py"]
