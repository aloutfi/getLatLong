import urllib3
import json
import os

GCP_API_KEY = os.getenv("GCP_API_KEY")


def call_google(address: str) -> dict:
    """Call google for the coordinates given the address."""
    http = urllib3.PoolManager()

    r = http.request(
        "GET",
        "https://maps.googleapis.com/maps/api/geocode/json",
        fields={"key": GCP_API_KEY, "address": address},
    )
    data = json.loads(r.data.decode("utf-8"))
    try:
        coords = data["results"][0]["geometry"]["location"]
    except IndexError:
        coords = {"lat": None, "lng": None}

    return coords
