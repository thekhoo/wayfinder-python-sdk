
from typing import List
from constants.places import PlaceType
from constants.transports import TransportType
from data.address import get_address_object_from_str
from data.places import get_all_nearby_places_by_place_type
from data.types import AddressResponse, PlacesNearby, PlacesNearbyResponse


def get_nearby_places_by_place_type_and_limit(
    origin: AddressResponse,
    place_type: PlaceType,
    limit: int
    ) -> List[PlacesNearby]:

    places_nearby = get_all_nearby_places_by_place_type(
        origin,
        place_type
    )

    places_to_get_directions : list[PlacesNearby] = (
        places_nearby[:limit]
        if len(places_nearby) > limit
        else places_nearby
    )

    return places_to_get_directions