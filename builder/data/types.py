from typing import List, Optional
from constants.transports import TransportType, TransitMode

class AddressResponse:

    def __init__(
            self, 
            address_response:list, 
            address_name:Optional[str]=None
    ) -> None:
        self.address_response = address_response[0] # In a single index array
        
        # Top Level Dict Items
        self.name = address_name # User input name to match and reduce confusion
        self.address_components = _AddressComponents(self.address_response.get("address_components"))
        self.formatted_address = self.address_response.get("formatted_address")
        self.geometry = _Geometry(self.address_response.get("geometry"))
        self.place_id = self.address_response.get("place_id")
        self.plus_code = _PlusCode(self.address_response.get("plus_code"))
        self.types = self.address_response.get("types")

        self.geocode = self.geometry.location

class PlacesNearbyResponse:

    def __init__(self,places_nearby_response:dict) -> None:

        self.places = [
            PlacesNearby(result) for 
            result in places_nearby_response.get('results')
        ]

        self.status : str = places_nearby_response.get('status')

class DirectionsResponse:

    def __init__(self, direction_response:list) -> None:
        direction_response = direction_response[0]
        # self.bounds = direction_response.get('bounds')

        legs = _Legs(direction_response.get("legs"))

        self.distance_in_m = legs.distance_in_m
        self.distance_in_text = legs.distance_in_text
        self.duration_in_s = legs.duration_in_s
        self.duration_in_text = legs.duration_in_text
        self.start_address = legs.start_address
        self.end_address = legs.end_address
        self.start_location = legs.start_location
        self.end_location = legs.end_location
        self.steps = legs.steps

    def __str__(self) -> str:
        return f"{self.end_address}\t|\t{self.distance_in_text}\t|\t{self.duration_in_text}"

class _Legs:

    def __init__(self, legs:list) -> None:
        if legs is not None:
            self.legs = legs[0]
            self.distance_in_m : int = self.legs.get("distance").get("value")
            self.distance_in_text : str = self.legs.get("distance").get("text")
            self.duration_in_s : int = self.legs.get("duration").get("value")
            self.duration_in_text : str = self.legs.get("duration").get("text")
            self.end_address : str = self.legs.get("end_address")
            self.end_location : dict[str,float] = self.legs.get("end_location")
            self.start_address : str = self.legs.get("start_address")
            self.start_location : dict[str,float] = self.legs.get('start_location')
            self.steps : list = [Step(step) for step in self.legs.get("steps")]

class Step:

    def __init__(self, step:dict) -> None:

        if step is not None:

            self.distance_in_m : int = step.get("distance").get("value")
            self.distance_in_text : str = step.get("distance").get("text")
            self.duration_in_s : int = step.get("duration").get("value")
            self.duration_in_text : str = step.get("duration").get("text")
            self.start_location : dict[str,float] = step.get('start_location')
            self.end_location : dict[str,float] = step.get("end_location")
            self.transport_type : TransportType = TransportType(step.get("travel_mode").lower())
            self.transit_details : TransitDetails = TransitDetails(step.get('transit_details'))

class TransitDetails:

    def __init__(self,transit_details:dict) -> None:
        self.transit_details = transit_details

        if transit_details is not None:
            self.arrival_stop = transit_details.get('arrival_stop')
            self.departure_stop = transit_details.get('departure_stop')
            self.line = _Line(transit_details.get('line'))
            self.headsign = transit_details.get('headsign')
            self.num_stops = transit_details.get('num_stops')

class _Line:

    def __init__(self,line:dict) -> None:
        self.line = line

        if line is not None:
            self.short_name = line.get('short_name')
            self.name = line.get('name')
            self.vehicle = TransitMode(line.get('vehicle').get('type').lower())
        
class PlacesNearby:

    def __init__(self,result:dict) -> None:

        if result is not None:
            self.business_status : str = result.get('business_status')
            self.geometry = _Geometry(result.get('geometry'))
            self.name : str = result.get('name')
            self.opening_hours : dict[str,bool] = result.get('opening_hours')
            self.place_id : str = result.get('place_id')
            self.plus_code = _PlusCode(result.get('plus_code'))
            self.rating : float = result.get('rating')
            self.types : List[str] = result.get('types')
            self.user_ratings_total : int = result.get('user_ratings_total')
            self.vicinity : str = result.get('vicinity')


class _AddressComponents:

    def __init__(self, address_components:list) -> None:

        # Array Indexes
        STREET_NUMBER = 0
        ROUTE = 1
        LOCALITY = 2
        ADMINISTRATIVE_AREA_LEVEL_2 = 3
        ADMINISTRATIVE_AREA_LEVEL_1 = 4
        COUNTRY = 5
        POSTAL_CODE = 6

        if address_components is not None:

            self.street_number = address_components[STREET_NUMBER]
            self.route = address_components[ROUTE]
            self.locality = address_components[LOCALITY]
            self.administrative_area_level_2 = address_components[ADMINISTRATIVE_AREA_LEVEL_2]
            self.administrative_area_level_1 = address_components[ADMINISTRATIVE_AREA_LEVEL_1]
            self.country = address_components[COUNTRY]
            self.postal_code = address_components[POSTAL_CODE]


class _Geometry:

    def __init__(self,geometry:dict) -> None:
        if geometry is not None:
            self.geometry = geometry
            self.location = geometry.get("location")
            self.location_type = geometry.get("location_type")
            self.viewport = _ViewPort(geometry.get("viewport"))

class _ViewPort:

    def __init__(self, viewport:dict) -> None:
        if viewport is not None:
            self.viewport = viewport
            self.northeast = viewport.get("northeast")
            self.southwest = viewport.get("southwest")

class _PlusCode:

    def __init__(self, plus_code:dict) -> None:
        if plus_code is not None:
            self.compound_code = plus_code.get("compound_code")
            self.global_code = plus_code.get("global_code")
        