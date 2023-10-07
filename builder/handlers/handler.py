import json
from core.logger import configure_logger, get_logger
from data.address import get_address_object_from_str
from handlers.config import SearchConfig
from service.places import get_nearby_places_by_place_type_and_limit
from service.directions import get_directions_for_multiple_places

logger = get_logger(__name__)

def handler(
    config: SearchConfig
):
    configure_logger()

    logger.info(f"Handler initiated")

    try:
        # Get the origin address and point of interests geocoded
        start_address_obj = get_address_object_from_str(config.start_address)
        logger.info(f"Starting search from origin address {config.get_json()}")

        # # Get the directions to point of interests
        logger.info("Getting directions for all places of interest from config")
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

        logger.info("Updating directions dictionary for all places of interest from config")
        poi_directions_dict = {
            "places_of_interest": poi_directions_list
        }

        # Get the directions to other search locations specified
        search_location_directions_dict : dict = {}
        logger.info("Getting directions for all nearby places by place type from config")
        for search_location in config.search_locations:
            logger.info(f"Getting nearby places for {search_location.place_type.value}")
            # Get the nearby places
            nearby_places = get_nearby_places_by_place_type_and_limit(
                origin=start_address_obj,
                place_type=search_location.place_type,
                limit=search_location.limit,
            )

            logger.info(f"Getting directions to {[nearby_place.name for nearby_place in nearby_places]}")
            # Get the directions to these nearby places
            directions_to_places_nearby = get_directions_for_multiple_places(
                origin=start_address_obj,
                destinations=nearby_places,
                transport_types=search_location.transport_modes,
                departure_time_str=search_location.departure_time_str,
                arrival_time_str=search_location.arrival_time_str
            )

            logger.info("Updating search locations dictionary for all nearby places from config")
            search_location_directions_dict.update({
                search_location.place_type.value: directions_to_places_nearby
            })

        return json.dumps({
            **poi_directions_dict,
            **search_location_directions_dict
        })
    except Exception as e:
        logger.error(e)