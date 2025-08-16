import csv

def read_birthdays(csv_file):
    """Reads member birthdays from a CSV file and returns a list of dictionaries."""
    birthdays = []

    #with makes sure the file is properly closed after reading.
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file) # turns row in dict format
        for row in reader:
            birthdays.append(row) # adds each row to the birthdays array as dict
    return birthdays

people = read_birthdays("birthdays.csv")

# print(people)