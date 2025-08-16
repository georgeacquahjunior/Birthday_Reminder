from reader import read_birthdays
from calendar_maker import create_calendar
from email_sender import send_email

if __name__ == "__main__":
    # Read birthdays
    birthdays = read_birthdays("birthdays.csv")

    # Create calendar
    ics_file = create_calendar(birthdays)

    # Send to council admin
    send_email("council_admin@example.com", "Council Birthday Calendar", "Here are the birthday reminder(s).", ics_file)
