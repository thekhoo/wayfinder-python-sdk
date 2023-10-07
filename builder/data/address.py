from googlemaps import geocoding
from data.types import AddressResponse
from core.googlemaps import get_googlemaps_client

def get_address_object_from_str(address:str) -> AddressResponse:
    client = get_googlemaps_client()
    return AddressResponse(
        geocoding.geocode(client,address),
        address
    )   

