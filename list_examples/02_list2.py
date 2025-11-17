import random

random_numbers = []
for i in range(5):
    number = random.randrange(1, 10)
    random_numbers.append(number)
print(random_numbers)

max_number = max(random_numbers)
print(f'max number is {max_number}')

my_max_number = 0
for i in range(len(random_numbers)):
    if random_numbers[i] > my_max_number:
        my_max_number = random_numbers[i]
print(f'my max number is {my_max_number}')