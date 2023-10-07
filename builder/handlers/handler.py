import json
from typing import List
from handlers.config import SearchConfig, LocationConfig, POIConfig
from constants.places import PlaceType
from constants.transports import TransportType
from data.address import get_address_object_from_str
from service.places import get_nearby_places_by_place_type_and_limit
from service.directions import get_directions_for_multiple_places

def handler(
    config: SearchConfig
):
    # Get the origin address and point of interests geocoded
    start_address_obj = get_address_object_from_str(config.start_address)

    # # Get the directions to point of interests
    poi_directions_list = list(
        map(
            lambda poi : get_directions_for_multiple_places(
                origin=start_address_obj,
                destinations= [get_address_object_from_str(poi.poi_name_or_address)],
                transport_types=poi.transport_modes,
                departure_time_str=poi.departure_time_str,
                arrival_time_str=poi.arrival_time_str
            )[0], # Should only have one place
            config.points_of_interest
        )
    )

    poi_directions_dict = {
        "places_of_interest": poi_directions_list
    }

    # Get the directions to other search locations specified
    search_location_directions_dict : dict = {}
    for search_location in config.search_locations:

        # Get the nearby places
        nearby_places = get_nearby_places_by_place_type_and_limit(
            origin=start_address_obj,
            place_type=search_location.place_type,
            limit=search_location.limit,
        )

        # Get the directions to these nearby places
        directions_to_places_nearby = get_directions_for_multiple_places(
            origin=start_address_obj,
            destinations=nearby_places,
            transport_types=search_location.transport_modes,
            departure_time_str=search_location.departure_time_str,
            arrival_time_str=search_location.arrival_time_str
        )

        search_location_directions_dict.update({
            search_location.place_type.value: directions_to_places_nearby
        })

    return json.dumps({
        **poi_directions_dict,
        **search_location_directions_dict
    })