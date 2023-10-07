from typing import List
from core.logger import get_logger
from constants.places import PlaceType
from data.places import get_all_nearby_places_by_place_type
from data.types import AddressResponse, PlacesNearby

logger = get_logger(__name__)

def get_nearby_places_by_place_type_and_limit(
    origin: AddressResponse,
    place_type: PlaceType,
    limit: int
    ) -> List[PlacesNearby]:

    logger.info(f"Getting place type '{place_type.value} nearby {origin}'")
    places_nearby = get_all_nearby_places_by_place_type(
        origin,
        place_type
    )

    logger.info(f"Shortening nearby places to {limit} results")
    places_to_get_directions : list[PlacesNearby] = (
        places_nearby[:limit]
        if len(places_nearby) > limit
        else places_nearby
    )

    return places_to_get_directions