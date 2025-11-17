import random

random_numbers = []
for i in range(5):
    number = random.randrange(1, 10)
    random_numbers.append(number)
print(random_numbers)

random_numbers.insert(-1, 1000)
print(random_numbers)