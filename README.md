# Wayfinder SDK

This is still a work in progress.

An SDK that is wrapping the `googlemaps` API using the Python `googlemaps` SDK Library.

> No, I'm not sure if calling this an SDK is technically correct but I won't be losing sleep over it so neither should you.

## Setup

Create an `.env` file in the root directory with the google maps API key that you have generated. An example `.example.env` file is a template that can be used. 

If you missed that, paste this in your `.env` file and place your API key in:

```
GOOGLE_MAPS_API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXX"
```

You can create a google maps API key [here](https://developers.google.com/maps/documentation/javascript/get-api-key).

In the CLI, run the following command to install the python modules required to use this app.

```bash
pip install -r requirements.txt
```

## Running the SDK

The entry point for this SDK is in `builder/app.py`. Before running the SDK, you must set up the `SearchConfig` within `app.py` so the SDK knows what to search for.

The config format is:

```py
config : SearchConfig = SearchConfig(
    start_address="Premier Inn London Leicester",
    points_of_interest=[
        POIConfig(
            poi_name_or_address="Borough Market",
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
```

* `start_address` would be the address of your origin

* `points_of_interest` is an array of `POIConfig` objects that allow you to explicitly specify the address/name of places that you wish to find directions to.

    * `poi_name_or_address` is the name or address of the point of interest

    * `transport_modes` is an array of `TransportType` enums compatible with the Google Maps API that allow you to specify which modes of transportation you wish to use

* `search_locations` is an array of `LocationConfig` objects that allow you to search by the types of places (i.e. Supermarkets, Train Stations)

    * `place_type` is an `PlaceType` enum compatible with the Google Maps API that allows you to specify the type of places to search for

    * `transport_modes` is an array of `TransportType` enums compatible with the Google Maps API that allow you to specify which modes of transportation you wish to use

    * `limit` limits the number of results to return

* `departure_time_str` and `arrival_time_str` are **optional parameters** that, when used, must be in the format "HH:MM:SS". The date defaults to the next day.

    * _Example: If today is `15/10/2023` and the time is set to `"11:32:00"`, the datetime used for directions will be `"16/10/2023 11:32:00"`_

Make sure the following imports are in `app.py` when building the config:

```py
from handlers.config import SearchConfig, LocationConfig, POIConfig
from constants.places import PlaceType
from constants.transports import TransportType
```

## Future Work

In order of priority... ish

* Format the results in a nicer way? (Maybe add functions to return the data in specific formats?)

    * Update 7/10/2023 - It now returns a JSON string so you can use a [JSON Beautifier](https://codebeautify.org/jsonviewer)

* Use an actual `.config` file instead of this half-ass config class object

* Introduce logging to the SDK to get a better idea of what's going on when and where it is in the execution callstack

* testtesttesttesttesttesttesttest

* Allowing users to specify the transit types when `TransportType.Transit` is selected (i.e. rail, tram, bus etc...)

## Footnote

This SDK (if you can even call it an SDK) was built by a person who was too lazy to keep on searching google maps when trying to find a place to rent. It's a miracle this even works.

See also:

* [Google Maps Python SDK](https://github.com/googlemaps/google-maps-services-python/tree/master)

* [Directions API](https://developers.google.com/maps/documentation/directions/)

* [Places API](https://developers.google.com/maps/documentation/places/web-service)

* [Geocoding API](https://developers.google.com/maps/documentation/geocoding/)

*I believe I only used these APIs in building this but hey, I'm only human and could be wrong*



