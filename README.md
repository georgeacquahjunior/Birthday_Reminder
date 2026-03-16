# Birthday Reminder

A simple Python automation project that:

1. Reads birthdays from a CSV file.
2. Generates an `.ics` calendar file with all-day birthday events.
3. Emails the generated calendar as an attachment.

This is useful for clubs, communities, churches, or teams that want a shared birthday reminder calendar.

## Project Structure

- `main.py` — Entry point; runs the complete workflow.
- `reader.py` — Reads birthday records from CSV.
- `calendar_maker.py` — Builds the `.ics` calendar file.
- `email_sender.py` — Sends the generated file by email.
- `birthdays.csv` — Source birthday data.
- `birthdays.ics` — Output calendar file (generated/updated).
- `requirements.txt` — Python dependencies.

## How It Works

When you run `main.py`:

- `read_birthdays("birthdays.csv")` loads member data.
- `create_calendar(...)` creates calendar events from each birthday.
- `send_email(...)` sends the `.ics` file to the configured recipient.

## Data Format (`birthdays.csv`)

Use this header and date format:

```csv
name,email,birthday
John Doe,john@example.com,1995-05-20
Mary Smith,mary@example.com,2000-08-10
```

- `birthday` must be in `YYYY-MM-DD` format.

## Setup

### 1) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
pip install python-dotenv
```

> Note: `email_sender.py` uses `python-dotenv`, so ensure it is installed.

### 3) Create a `.env` file

In the project root, add:

```env
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_app_password
```

For Gmail, use an **App Password** if 2FA is enabled.

## Run the Project

```bash
python main.py
```

If successful, the script will:

- Generate (or overwrite) `birthdays.ics`.
- Send an email with the calendar attached.

## Notes

- The current email code targets Gmail SMTP.
- Keep your `.env` file private and never commit real credentials.
- You can change the recipient, subject, and body in `main.py`.

## Troubleshooting

- **`ModuleNotFoundError`**: install missing packages in your virtual environment.
- **Date parsing errors**: verify birthdays are valid `YYYY-MM-DD` dates.
- **SMTP/authentication errors**:
  - confirm `EMAIL_USER` and `EMAIL_PASS` are correct,
  - use an app password,
  - verify the SMTP settings required by your provider.

## Possible Improvements

- Add recurring yearly birthday events in the calendar.
- Filter reminders to upcoming birthdays only.
- Add CLI options (input CSV path, recipient email, output file).
- Add tests for CSV parsing and calendar generation.
