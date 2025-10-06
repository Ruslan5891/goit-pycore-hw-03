import random


def get_numbers_ticket(min, max, quantity):

    if (type(min) != int or type(max) != int or type(quantity) != int):
        return 'All values must be an integer'

    if (min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1)):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


print('Your lucky numbers are: ', get_numbers_ticket("1", 46, 6))
print('Your lucky numbers are: ', get_numbers_ticket(0, 46, 6))
print('Your lucky numbers are: ', get_numbers_ticket(1, 10, 3))
print('Your lucky numbers are: ', get_numbers_ticket(1, 46, 6))
