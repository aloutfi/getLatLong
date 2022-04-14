from fastapi import FastAPI
from app.call_google import call_google
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="GetLatLong API", redoc_url="/", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get")
async def get_coords(address: str):
    """Given an address, return the corresponding coordinates."""
    return call_google(address)
