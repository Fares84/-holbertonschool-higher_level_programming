#!/usr/bin/python3
for number in range(0, 90):
    if number == 89:
        print("{:d}".format(number))
    else:
        (number / 10) < (number % 10)
        print("{:02d}".format(number), end=', ')
