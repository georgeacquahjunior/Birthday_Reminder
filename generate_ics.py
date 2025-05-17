from ics import Calendar, Event
from datetime import datetime

def create_birthday_ics(birthdays, output_file = "birthdays.ics"):
    calendar = Calendar()
    for person in birthdays:
        event = Event()
        event.name = f"Birthday: {person['name']}"
        event.begin = datetime.now().date().isoformat()
        event.make_all_day()
        event.description = f"Wish {person['name']} a happy birthday!"
        calendar.events.add(event)

        with open(output_file, 'w') as f:
            f.writelines(calendar)

        return output_file