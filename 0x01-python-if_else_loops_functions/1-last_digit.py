#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = number % 10
if s > 5:
    print(f"Last digit of {number:d} is {s:d} and is greater than 5")
elif s < 6 and s != 0:
    print(f"Last digit of {number:d} is {s:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {s:d} and is 0")
