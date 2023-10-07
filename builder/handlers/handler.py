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
    poi_directions_dict = {}
    for poi in config.points_of_interest:
        directions = get_directions_for_multiple_places(
            origin=start_address_obj,
            destinations= [get_address_object_from_str(poi.poi_name_or_address)],
            transport_types=poi.transport_modes
        )

        poi_directions_dict.update({
            poi.poi_name_or_address: directions
        })

    # Get the directions to other search locations specified
    search_location_directions_dict : dict = {}
    for search_location in config.search_locations:

        # Get the nearby places
        nearby_places = get_nearby_places_by_place_type_and_limit(
            origin=start_address_obj,
            place_type=search_location.place_type,
            limit=search_location.limit
        )

        # Get the directions to these nearby places
        directions_to_places_nearby = get_directions_for_multiple_places(
            origin=start_address_obj,
            destinations=nearby_places,
            transport_types=search_location.transport_modes
        )

        search_location_directions_dict.update({
            search_location.place_type.value: directions_to_places_nearby
        })

    return {
        **poi_directions_dict,
        **search_location_directions_dict
    }

if __name__ == '__main__':
    config : SearchConfig = SearchConfig(
        start_address="Flat 3, 38-40 Crown Street, Reading RG1 2SE",
        points_of_interest=[
            POIConfig(
                poi_name_or_address="Aurora Energy Research",
                transport_modes=[TransportType.Transit]
            ),
            POIConfig(
                poi_name_or_address="Sweco Maidenhead",
                transport_modes=[TransportType.Transit]
            )
        ],
        search_locations=[
            LocationConfig(
                place_type=PlaceType.Supermarket,
                transport_modes=[
                    TransportType.Bicycling,
                    TransportType.Transit,
                ]
            ),
            LocationConfig(
                place_type=PlaceType.TrainStation,
                transport_modes=[
                    TransportType.Walking,
                    TransportType.Bicycling
                ],
                limit=2
            )
        ] 
    )

    result = handler(config)