from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gateway")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Gateway iniciado. Preparando conexões externas...")
    yield
    # Shutdown
    logger.info("Gateway finalizando. Encerrando conexões...")

app = FastAPI(title="Karnak Gateway", version="0.1.0", lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Gateway online 🚀"}

@app.get("/health")
def healthcheck():
    return {"status": "ok"}