#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

print(f"Last digit of {number} is {last_digit}", end=" ")

if number < 0:
    print("less than 6 and not 0" if last_digit != 0 else "0")
else:
    print("greater than 5")
