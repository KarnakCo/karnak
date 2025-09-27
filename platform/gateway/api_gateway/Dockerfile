FROM python:3.11-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os módulos comuns e o gateway
COPY platform/common /app/platform/common
COPY platform/gateway/api_gateway /app/platform/gateway/api_gateway

# Instala dependências principais
RUN pip install --no-cache-dir fastapi uvicorn nats-py kafka-python pyjwt prometheus-client opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation

# Expõe a porta que o Render espera
EXPOSE 8080

# Comando para iniciar o FastAPI via Uvicorn
CMD ["uvicorn", "platform.gateway.api_gateway.main:app", "--host", "0.0.0.0", "--port", "8080"]
