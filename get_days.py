from datetime import datetime, timedelta


def get_days_from_today(date):
    if type(date) != str:
        return "Entered data must be a string"

    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        return "Invalid date or format. Use 'YYYY-MM-DD', for example: 2025-10-01"


print(get_days_from_today(2021))
print(get_days_from_today(2021-10-0))
print(get_days_from_today("2020.10.09"))
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-10-10"))