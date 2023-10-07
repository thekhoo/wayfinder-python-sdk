from enum import Enum

class TransitMode(str, Enum):
    """Rail is the equivalent to train, tram and subway"""
    Bus = "bus"
    Subway = "subway"
    Train = "train"
    Tram = "tram"
    Rail = "rail"
    HeavyRail = "heavy_rail"

class TransportType(str,Enum):
    Driving = "driving"
    Walking = "walking"
    Bicycling = "bicycling"
    Transit = "transit"
