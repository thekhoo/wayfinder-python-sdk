from enum import Enum

class TransitMode(str, Enum):
    """Rail is the equivalent to train, tram and subway"""
    Bus = "bus"
    Subway = "subway"
    Train = "train"
    Tram = "tram"
    Rail = "rail"
    _HeavyRail = "heavy_rail"
    _IntercityBus = "intercity_bus"

class TransportType(str,Enum):
    Driving = "driving"
    Walking = "walking"
    Bicycling = "bicycling"
    Transit = "transit"
