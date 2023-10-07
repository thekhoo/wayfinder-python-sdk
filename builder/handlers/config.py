import json
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

    def get_json(self):
        return json.dumps(
            {
                "place_type": self.place_type.value,
                "transport_modes": [transport_mode.value for transport_mode in self.transport_modes],
                "limit": self.limit,
                "departure_time_str": self.departure_time_str,
                "arrival_time_str": self.arrival_time_str
            }
        )


@dataclass
class POIConfig:

    poi_name_or_address: str
    transport_modes: List[TransportType]
    departure_time_str: Optional[datetime] = None
    arrival_time_str: Optional[datetime] = None

    def get_json(self):
        return json.dumps(
            {
                "poi_name_or_address": self.poi_name_or_address,
                "transport_modes": [transport_mode.value for transport_mode in self.transport_modes],
                "departure_time_str": self.departure_time_str,
                "arrival_time_str": self.arrival_time_str
            }
        )

@dataclass
class SearchConfig:

    start_address: str
    points_of_interest: List[POIConfig]
    search_locations: List[LocationConfig]

    def get_json(self):
        return json.dumps(
            {
                "start_address": self.start_address,
                "points_of_interest": [poi.get_json() for poi in self.points_of_interest],
                "search_locations": [search_location.get_json() for search_location in self.search_locations]
            },
            indent=4
        )

