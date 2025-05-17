import csv
from datetime import datetime

def get_today_birthdays(csv_file):
    today = datetime.today()
    birthdays = []

    with open(csv_file, newline = '') as file:
        reader = csv.DictReader(file)
        for row in reader:
            birth_date = datetime.strptime(row['birthday'], '%Y-%m-%d')
            if birth_date.month == today.month and birth_date.day == today.day:
                birthdays.append({
                    "name": row['name'],
                    "email": row['email'],
                    "birthday": birth_date
                })
    return birthdays