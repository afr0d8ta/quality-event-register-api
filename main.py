
from fastapi import FastAPI

app = FastAPI(
    title="Quality Event Register API",
    description="A demonstration REST API for manufacturing quality events.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Quality Event Register API is running",
        "status": "success",
        "version": "0.1.0"
    }


from fastapi import FastAPI

app = FastAPI(
    title="Quality Event Register API",
    description="A demonstration REST API for manufacturing quality events.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Quality Event Register API is running",
        "status": "success",
        "version": "0.1.0"
    }

