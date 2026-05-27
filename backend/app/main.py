from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Production Grade Kubernetes Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/version")
def version():
    return {
        "version": "v1"
    }