from fastapi import FastAPI
import logging

# Inicializa o app FastAPI
app = FastAPI(title="Karnak Gateway", version="0.1.0")

# Configura logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gateway")

@app.get("/")
def root():
    return {"message": "Gateway online 🚀"}

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

# 🔜 Aqui no futuro você pode adicionar integração com NATS, Kafka, etc.
# Exemplo de placeholder:
@app.on_event("startup")
async def startup_event():
    logger.info("Gateway iniciado. Preparando conexões externas...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Gateway finalizando. Encerrando conexões...")