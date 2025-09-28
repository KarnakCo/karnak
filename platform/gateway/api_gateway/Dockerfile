FROM python:3.11-slim

WORKDIR /app

# Copia tudo que está nesse diretório (inclui main.py)
COPY . /app

# Instala dependências
RUN pip install --no-cache-dir fastapi uvicorn nats-py kafka-python pyjwt prometheus-client opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation

EXPOSE 8080
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]