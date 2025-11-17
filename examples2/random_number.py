import random

number = random.randrange(1, 10)
result = ()

for i in range(3):
    my_number = int(input("Take a guess:  "))
    if my_number == number:
        print('Congratulations!')
        break
    else:
        print("Sorry!")

else:
    print(f"The random digit is {number}")

