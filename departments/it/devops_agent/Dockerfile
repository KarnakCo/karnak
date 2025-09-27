FROM python:3.11-slim
WORKDIR /app
COPY platform/common /app/platform/common
COPY departments/it/devops_agent /app/departments/it/devops_agent
RUN pip install --no-cache-dir nats-py kafka-python prometheus-client opentelemetry-sdk opentelemetry-exporter-otlp
CMD ["python", "/app/departments/it/devops_agent/main.py"]
