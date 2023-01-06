#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check last digits of negative and positive numbers
if number >= 0:
    l_dig = number % 10
else:
    l_dig = number % -10

print(f'Last digit of {number} is {l_dig}', end=' ')
if l_dig > 5:
    print('and is greater than 5')
elif 6 > l_dig != 0:
    print('and is less than 6 and not 0')
else:
    print('and is 0')
