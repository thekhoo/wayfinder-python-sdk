from googlemaps import geocoding
from data.types import AddressResponse
from core.logger import get_logger
from core.googlemaps import get_googlemaps_client

logger = get_logger(__name__)

def get_address_object_from_str(address:str) -> AddressResponse:
    client = get_googlemaps_client()
    logger.info(f"Getting Google Maps API Response for Geocoding {address}")
    return AddressResponse(
        geocoding.geocode(client,address),
        address
    )   

