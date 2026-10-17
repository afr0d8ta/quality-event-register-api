
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

@app.get("/quality-events", summary="List simulated quality events")
def get_quality_events():
    """Return two fictional manufacturing quality events for demonstration."""
    return [
        {
            "event_id": "QE-2026-0001",
            "event_type": "Deviation",
            "title": "Packaging seal integrity failure",
            "severity": "Major",
            "status": "Open"
        },
        {
            "event_id": "QE-2026-0002",
            "event_type": "Nonconformance",
            "title": "Finished product outside weight specification",
            "severity": "Minor",
            "status": "Under Investigation"
        }
    ]