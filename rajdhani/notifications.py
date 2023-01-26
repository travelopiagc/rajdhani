"""Email notifications on bookings.
"""
from . import config
from smtplib import SMTP as Client

def send_booking_confirmation_email(booking):
    """Sends a confirmation email on successful booking.

    The argument `booking` is a row in the database that contains the following fields:

        id, name, email, train_number, train_name, ticket_class, date
    """
    # The smtp configuration is available in the config module
    
    client = Client(config.smtp_hostname, config.smtp_port)
    
    r=client.sendmail(booking["passenger_email"], 'giedrius.ceginskas@travelopia.com',"""\
        Train {train_number}:{ticket_class}, Date {date}, Passenger: {passenger_name} ({passenger_email}) \
         """.format(**booking))
    
    pass
