#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
msg = "Last digit of {:d} is {:d} and is ".format(number, last_digit)
if last_digit > 5:
	msg += "greater than 5"
elif last_digit == 0:
	msg += "0"
else:
	msg += "less than 6 and not 0"
print(msg)
