from ics import Calendar, Event # Python library for creating calendar files
from datetime import datetime

def create_calendar(birthdays, output_file="birthdays.ics"):
    """Creates an .ics calendar file from the list of birthdays."""
    calendar = Calendar() # Makes an empty calendar object where we’ll add events (birthdays)

    for person in birthdays:
        name = person["name"] # retrieve name
        birthday = datetime.strptime(person["birthday"], "%Y-%m-%d").date() # converts string date to real date object

        # Create birthday event
        event = Event()
        event.name = f"{name}'s Birthday !!" # sets the title
        event.begin = birthday.strftime("%Y-%m-%d") # sets the start date of the event and take date back to string
        event.make_all_day() # makes it an all-day event

        calendar.events.add(event) # adds this new event into the calendar.

    # Save the .ics file
    with open(output_file, "w") as f:
        f.writelines(calendar)
    return output_file
