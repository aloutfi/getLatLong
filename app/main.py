from fastapi import FastAPI
from app.call_google import call_google

app = FastAPI(title="GetLatLong API", redoc_url="/", version="1.0.0")


@app.get("/get")
async def get_coords(address: str):
    """Given an address, return the corresponding coordinates."""
    return call_google(address)
