"""
Module to interact with the database.
"""

from . import db_ops

db_ops.ensure_db()


def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation

    return [
        {"code": "SBC", "name": "Bangalore"},
        {"code": "MAS", "name": "Chennai"},
        {"code": "NDLS", "name": "New Delhi"},
        {"code": "MMCT", "name": "Mumbai"}
    ]

def search_trains(from_station, to_station, date, ticket_class):
    """Returns all the trains that source to destination stations on
    the given date. When ticket_class is provided, this should return
    only the trains that have that ticket class.

    This is used to get show the trains on the search results page.
    """
    # TODO: make a db query to get the matching trains
    # and replace the following dummy implementation

    return [
        {
            "number": "12028",
            "name": "Shatabdi Exp",
            "from_station_code": "SBC",
            "from_station_name": "Bangalore",
            "to_station_code": "MAS",
            "to_station_name": "Chennai",
            "departure": "06:00",
            "arrival": "11:00",
            "duration_h": 5,
            "duration_m": 0
        },
        {
            "number": "12608",
            "name": "Lalbagh Exp",
            "from_station_code": "SBC",
            "from_station_name": "Bangalore",
            "to_station_code": "MAS",
            "to_station_name": "Chennai",
            "departure": "06:20",
            "arrival": "12:15",
            "duration_h": 5,
            "duration_m": 55
        },
    ]
