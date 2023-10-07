from typing import List, TypedDict
from dataclasses import dataclass
from constants.places import PlaceType
from constants.transports import TransportType

@dataclass
class LocationConfig:

    place_type: PlaceType
    transport_modes: List[TransportType]
    limit: int = 3

@dataclass
class POIConfig:

    poi_name_or_address: str
    transport_modes: List[TransportType]

@dataclass
class SearchConfig:

    start_address: str
    points_of_interest: List[POIConfig]
    search_locations: List[LocationConfig]

