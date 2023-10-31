#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

print("Last digit of", end=" ")
if last_digit > 5:
    print("{0} is {1} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("{0} is {1} and is 0".format(number, last_digit))
else:
    print("{0} is {1} and is less than 6 and not 0".format(number, last_digit))
