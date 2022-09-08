"""
Module to interact with the database.
"""

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
