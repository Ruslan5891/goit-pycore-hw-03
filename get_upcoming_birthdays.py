from datetime import datetime, timedelta

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


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Doe", "birthday": "1990.10.11"},
    {"name": "Test User", "birthday": "1990.10.08"}

]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
