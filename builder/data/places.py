from typing import List
from googlemaps import places
from data.types import AddressResponse, PlacesNearbyResponse, PlacesNearby
from constants.places import PlaceType
from core.googlemaps import get_googlemaps_client
from core.logger import get_logger

logger = get_logger(__name__)

def get_all_nearby_places_by_place_type(
        address_object:AddressResponse,
        place_type: PlaceType
) ->  List[PlacesNearby] :
    client = get_googlemaps_client()
    logger.info(f"Getting Google Maps API Response for Places Nearby for place type '{place_type.value}' near {address_object.name}")
    return PlacesNearbyResponse(
        places.places_nearby(
            client,
            address_object.geocode,
            type=place_type.value,
            rank_by="distance"
        )
    ).places