"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops
from sqlalchemy import create_engine, text, MetaData, Table, select, func, or_

db_ops.ensure_db()

# config has 'db_uri' that can be used to connect to the database
from . import config

def search_trains(
        from_station_code,
        to_station_code,
        ticket_class=None,
        departure_date=None,
        departure_time=[],
        arrival_time=[]):
    """Returns all the trains that source to destination stations on
    the given date. When ticket_class is provided, this should return
    only the trains that have that ticket class.

    This is used to get show the trains on the search results page.
    """
    # TODO: make a db query to get the matching trains
    # and replace the following dummy implementation'
    
    

    engine = create_engine(config.db_uri, echo=True)
    meta = MetaData(bind=engine)
    # meta.reflect(engine)
    # for table in meta.tables.values():
    #     print("Table name: ", table.name)
    #     for column in table.c:
    #         print("Column: ", column.name)
    
    train_table = Table("train", meta, autoload=True)
    station_table = Table("station", meta, autoload=True)
    booking_table = Table("booking", meta, autoload=True)
    schedule_table = Table("schedule", meta, autoload=True)

    t = train_table
    s = station_table
    b = booking_table
    sch = schedule_table
   
   
    
   
    ticket_class_search=(or_((t.c.sleeper == 1 and ticket_class=='SL')
         ,(t.c.second_ac == 1 and ticket_class=='2A')
         ,(t.c.first_ac == 1 and ticket_class=='1A')
         ,(t.c.first_class == 1 and ticket_class=='FC')
         ,(t.c.chair_car == 1 and ticket_class=='CC'))
                         ).label("ticket_class")
   

    q = (
        #select([text('*')])
        select(t.c.number
          ,t.c.name
          ,t.c.from_station_code
          ,t.c.from_station_name
          ,t.c.to_station_code
          ,t.c.to_station_name
          ,t.c.departure
          ,t.c.arrival
          ,t.c.duration_h
          ,t.c.duration_m
          )
        .where(t.c.from_station_code == from_station_code)
        .where(t.c.to_station_code == to_station_code) 
        .where(ticket_class_search)
    )

    rows = q.execute()
    
    return rows

def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation
    return placeholders.AUTOCOMPLETE_STATIONS

def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    return placeholders.SCHEDULE

def book_ticket(train_number, ticket_class, departure_date, passenger_name, passenger_email):
    """Book a ticket for passenger
    """
    # TODO: make a db query and insert a new booking
    # into the booking table

    return placeholders.TRIPS[0]

def get_trips(email):
    """Returns the bookings made by the user
    """
    # TODO: make a db query and get the bookings
    # made by user with `email`

    return placeholders.TRIPS
