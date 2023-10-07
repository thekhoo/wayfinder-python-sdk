from datetime import datetime
from handlers.handler import handler
from handlers.config import SearchConfig, LocationConfig, POIConfig
from constants.places import PlaceType
from constants.transports import TransportType

# Generate the search configuration
config : SearchConfig = SearchConfig(
    start_address="XXXXXXXXXXXXXXXXX",
    points_of_interest=[
        POIConfig(
            poi_name_or_address="XXXXXXXXXXXXXXXXX",
            transport_modes=[TransportType.Transit],
            departure_time_str="07:00:00"  # Must be in 24-hour format (i.e. "11:59:59")
        )
    ],
    search_locations=[
        LocationConfig(
            place_type=PlaceType.Supermarket,
            transport_modes=[
                TransportType.Bicycling,
                TransportType.Transit,
            ],
            limit=2,
            departure_time_str="07:00:00" # Must be in 24-hour format (i.e. "11:59:59")
        )
    ] 
)

if __name__ == '__main__':
    result = handler(config)