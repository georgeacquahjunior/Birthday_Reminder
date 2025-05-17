from read_birthdays import get_today_birthdays
from generate_ics import create_birthday_ics
from send_email import send_email_with_ics

def main():
    birthdays = get_today_birthdays("birthdays.csv")
    if birthdays:
        ics_file = create_birthday_ics(birthdays)
        send_email_with_ics("admin_email@example.com", ics_file)
    else:
        print("No birthdays today.")

if __name__ == "__main__":
    main()
