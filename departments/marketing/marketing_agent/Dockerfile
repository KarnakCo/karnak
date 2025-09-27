FROM python:3.11-slim
WORKDIR /app
COPY platform/common /app/platform/common
COPY departments/marketing/marketing_agent /app/departments/marketing/marketing_agent
RUN pip install --no-cache-dir nats-py kafka-python prometheus-client opentelemetry-sdk opentelemetry-exporter-otlp
CMD ["python", "/app/departments/marketing/marketing_agent/main.py"]
