from typing import List, Union
from datetime import datetime
from core.logger import get_logger
from constants.transports import TransportType
from data.directions import get_directions_by_transport_type_and_place_id
from data.types import AddressResponse, DirectionsResponse, PlacesNearby, Step
from utils.directions import get_datetime_from_str

logger = get_logger(__name__)

def get_directions_for_multiple_places(
    origin: AddressResponse,
    destinations: Union[List[PlacesNearby],List[AddressResponse]],
    transport_types: List[TransportType],
    departure_time_str:str=None,
    arrival_time_str:str=None
):
    origin_address = origin.formatted_address

    logger.info("Converting time string to datetime object")
    departure_time = get_datetime_from_str(departure_time_str) if departure_time_str is not None else None
    arrival_time = get_datetime_from_str(arrival_time_str) if arrival_time_str is not None else None

    directions = list(
        map(
            lambda destination : _get_directions_for_place(
                origin_address,
                destination,
                transport_types,
                departure_time,
                arrival_time
            ),
            destinations
        )
    )

    return directions

def _get_directions_for_place(
    origin_address: str,
    destination: Union[PlacesNearby, AddressResponse],
    transport_types: List[TransportType],
    departure_time:datetime=None,
    arrival_time:datetime=None
):
    destination_name : str = destination.name

    logger.info(f"Getting directions by transport types: {[transport.value for transport in transport_types]}")
    direction_by_transport_type : list[dict[TransportType, DirectionsResponse]] = list(
        map(
            lambda transport_type : _get_directions_for_place_by_transport(
                origin_address,
                destination.place_id,
                transport_type,
                departure_time,
                arrival_time
            ),
            transport_types
        )
    )

    return {destination_name: direction_by_transport_type}

def _get_transit_detail_from_step(
        step: Step
):
    
    additional_data = {}

    if step.transport_type == TransportType.Transit and step.transit_details is not None:
        logger.info("Getting additional step data for transit transport type")
        transit_details = step.transit_details

        additional_data.update({
            "additional_data": {
                "departure_stop": transit_details.departure_stop,
                "arrival_stop": transit_details.arrival_stop,
                "vehicle" : transit_details.line.vehicle,
                "vehicle_name": transit_details.line.name,
                "vehicle_short_name": transit_details.line.short_name,
                "headsign": transit_details.headsign,
                "num_stops": transit_details.num_stops
            }
        })
        
    return {
        step.transport_type: {
            "distance": {
                "value": step.distance_in_m,
                "text": step.distance_in_text
            },
            "duration": {
                "value": step.duration_in_s,
                "text": step.duration_in_text
            },
            **additional_data
        }
    }
    

def _get_directions_for_place_by_transport(
    origin_address: str,
    destination_id: str,
    transport_type: TransportType,
    departure_time:datetime=None,
    arrival_time:datetime=None
) -> DirectionsResponse:
    
    additional_details = {}
    
    logger.info(f"Getting directions to [destination_id: {destination_id}] using transport type '{transport_type.value}'")
    directions : DirectionsResponse = get_directions_by_transport_type_and_place_id(
                                            origin=origin_address,
                                            destination_id=destination_id,
                                            transport_type=transport_type,
                                            departure_time=departure_time,
                                            arrival_time=arrival_time
                                        )

    if transport_type == TransportType.Transit:
        # NOTE: Only need the steps for transit mode
        step_details = list(
            map(
                lambda step : _get_transit_detail_from_step(step),
                directions.steps
            )
        )

        additional_details.update({
            "additional_details": step_details
        })
    
    return {
        transport_type: {
            "distance" : {
                "text": directions.distance_in_text,
                "value": directions.distance_in_m
            },
            "duration": {
                "text": directions.duration_in_text,
                "value": directions.duration_in_s
            },
            **additional_details
        }
    }
    