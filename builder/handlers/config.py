from typing import List, Optional
from datetime import datetime
from dataclasses import dataclass
from constants.places import PlaceType
from constants.transports import TransportType

@dataclass
class LocationConfig:

    place_type: PlaceType
    transport_modes: List[TransportType]
    limit: int = 3
    departure_time_str: Optional[str] = None
    arrival_time_str: Optional[str] = None

@dataclass
class POIConfig:

    poi_name_or_address: str
    transport_modes: List[TransportType]
    departure_time_str: Optional[datetime] = None
    arrival_time_str: Optional[datetime] = None

@dataclass
class SearchConfig:

    start_address: str
    points_of_interest: List[POIConfig]
    search_locations: List[LocationConfig]

