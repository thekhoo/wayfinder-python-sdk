from typing import List
from googlemaps import places
from data.types import AddressResponse, PlacesNearbyResponse, PlacesNearby
from constants.places import PlaceType
from core.googlemaps import get_googlemaps_client

def get_all_nearby_places_by_place_type(
        address_object:AddressResponse,
        place_type: PlaceType
) ->  List[PlacesNearby] :
    client = get_googlemaps_client()
    return PlacesNearbyResponse(
        places.places_nearby(
            client,
            address_object.geocode,
            type=place_type.value,
            rank_by="distance"
        )
    ).places