from datetime import datetime
from googlemaps import directions
from constants.transports import TransitMode, TransportType
from core.googlemaps import get_googlemaps_client
from data.types import DirectionsResponse

def get_directions_by_transport_type(
    origin: str,
    destination: str,
    transport_type: TransportType,
    departure_time: datetime = None,
    arrival_time: datetime = None,
    transit_mode: TransitMode = None
) :
    
    gmaps_client = get_googlemaps_client()
    
    if transport_type is not TransportType.Transit and transit_mode is not None:
        raise Exception("Cannot specify a transit type for a non transit mode of transport")
    
    if departure_time and arrival_time:
        raise Exception("Cannot specify both departure and arrival time")
    
    return DirectionsResponse(
        directions.directions(
            gmaps_client,
            origin,
            destination,
            transport_type.value,
            units="metric",
            departure_time=departure_time,
            arrival_time=arrival_time,
            transit_mode=transit_mode.value if transit_mode is not None else None
        )
    )

def get_directions_by_transport_type_and_place_id(
    origin: str,
    destination_id: str,
    transport_type: TransportType,
    departure_time: datetime = None,
    arrival_time: datetime = None,
    transit_mode: TransitMode = None
) :
    
    gmaps_client = get_googlemaps_client()
    
    if transport_type is not TransportType.Transit and transit_mode is not None:
        raise Exception("Cannot specify a transit type for a non transit mode of transport")
    
    if departure_time and arrival_time:
        raise Exception("Cannot specify both departure and arrival time")
    
    return DirectionsResponse(
        directions.directions(
            gmaps_client,
            origin,
            f"place_id:{destination_id}",
            transport_type.value,
            units="metric",
            departure_time=departure_time,
            arrival_time=arrival_time,
            transit_mode=transit_mode.value if transit_mode is not None else None
        )
    )
    
