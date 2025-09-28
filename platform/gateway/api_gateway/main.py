from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gateway online 🚀"}

@app.get("/health")
def healthcheck():
    return {"status": "ok"}