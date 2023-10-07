from dotenv import load_dotenv
from googlemaps import Client
import os

load_dotenv()

def get_googlemaps_client() -> Client:
    api_key = os.environ["GOOGLE_MAPS_API_KEY"]
    return Client(key=api_key)