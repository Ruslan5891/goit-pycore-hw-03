from datetime import datetime, timedelta
import re
import random


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


def get_numbers_ticket(min, max, quantity):

    if (type(min) != int or type(max) != int or type(quantity) != int):
        return 'All values must be an integer'

    if (min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1)):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


def normalize_phone(phone_number):

    # We don't have any restrictions about type but add this check type for better code performing and don't throw an error
    if type(phone_number) != str:
        return phone_number

    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())

    if cleaned_number.startswith('+380'):
        return cleaned_number
    elif cleaned_number.startswith('380'):
        return '+' + cleaned_number
    elif cleaned_number.startswith('+'):
        return cleaned_number
    else:
        return '+38' + cleaned_number


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        original_birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = original_birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            greeting = birthday_this_year
            if greeting.weekday() == 5:
                greeting += timedelta(days=2)
            elif greeting.weekday() == 6:
                greeting += timedelta(days=1)

            result.append({
                "name": user["name"],
                "greeting": greeting.strftime("%Y.%m.%d")
            })

    return result
