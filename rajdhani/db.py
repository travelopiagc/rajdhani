"""
Module to interact with the database.
"""

from . import placeholders
from . import db_ops
from sqlalchemy import create_engine, text, MetaData, Table, select, func, or_, and_, between
from datetime import datetime

db_ops.ensure_db()

# config has 'db_uri' that can be used to connect to the database
from . import config

time_format = '%H:%M:%S'

time_ranges={} 
time_ranges["slot1"]= (datetime.strptime("00:00:00", time_format).time(),datetime.strptime("08:00:00", time_format).time())
time_ranges["slot2"]= (datetime.strptime("08:00:00", time_format).time(),datetime.strptime("12:00:00", time_format).time())
time_ranges["slot3"]= (datetime.strptime("12:00:00", time_format).time(),datetime.strptime("16:00:00", time_format).time())
time_ranges["slot4"]= (datetime.strptime("16:00:00", time_format).time(),datetime.strptime("20:00:00", time_format).time())
time_ranges["slot5"]= (datetime.strptime("20:00:00", time_format).time(),datetime.strptime("23:59:59", time_format).time())
    
engine = create_engine(config.db_uri, echo=True)
meta = MetaData(bind=engine)   
train_table = Table("train", meta, autoload=True)
station_table = Table("station", meta, autoload=True)
booking_table = Table("booking", meta, autoload=True)
schedule_table = Table("schedule", meta, autoload=True)

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

    

    t = train_table
   
        
    ticket_class_search = ticket_class_searches(t, ticket_class)
    departure_time_search, arrival_time_search = train_time_searches(t, departure_time, arrival_time)  

    q = (
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
        .where(or_(ticket_class_search))
        .where(or_(*departure_time_search))
        .where(or_(*arrival_time_search))
        
    )

    rows = q.execute()
    # for row in rows:
    #     print(row)
    
    return rows

def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    
    s = station_table
    b = booking_table
    sch = schedule_table
    
    
    
    query = (
        select(s.c.code
          ,s.c.name
          )
        .where(or_(func.lower(s.c.name).contains(q.lower()),func.lower(s.c.code).like(q.lower() + '%')))
        .limit(10)
    )

    rows = query.execute()
    stations=[]
    for row in rows:
        stations.append({"code": row.code, "name":row.name})
    return stations
   

def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    s = schedule_table
    
    query = (
        select(s.c.station_code
          ,s.c.station_name
          ,s.c.day
          ,s.c.arrival
          ,s.c.departure
          )
        .where(s.c.train_number==train_number)
    )
    
    rows = query.execute()
    # for row in rows:
    #     print(row)
        
    return rows

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


def time_in_a_range(train_time, range):
    return between(func.strftime(time_format,train_time), range[0], range[1])

def train_time_searches(t, departure_time, arrival_time):   
    departure_time_search = []
    for dep_time in departure_time:
        departure_time_search.append(and_(time_in_a_range(t.c.departure, time_ranges[dep_time])))
        
    arrival_time_search = []
    for arr_time in arrival_time:
        arrival_time_search.append(and_(time_in_a_range(t.c.arrival,time_ranges[arr_time])))
        
    return departure_time_search, arrival_time_search

def ticket_class_searches(t, ticket_class):
    if ticket_class == 'SL':
        return (t.c.sleeper == 1).label("SL")
    elif  ticket_class=='2A':
        return (t.c.second_ac == 1).label("2A")
    elif ticket_class=='1A':
        return (t.c.first_ac == 1).label("1A")
    elif ticket_class=='FC':
        return (t.c.first_class == 1).label("FC")
    elif ticket_class=='CC':
        return (t.c.chair_car == 1).label("CC")
    else:
        return text("1==1")