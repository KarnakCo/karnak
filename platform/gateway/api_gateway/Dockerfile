FROM python:3.11-slim
WORKDIR /app
COPY platform/common /app/platform/common
COPY platform/gateway/api_gateway /app/platform/gateway/api_gateway
RUN pip install --no-cache-dir fastapi uvicorn nats-py kafka-python pyjwt prometheus-client opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation
EXPOSE 8080
CMD ["python", "/app/platform/gateway/api_gateway/main.py"]
