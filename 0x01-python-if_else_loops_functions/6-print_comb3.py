#!/usr/bin/python3
for number_1 in range(10):
    for number_2 in range(number_1 + 1, 10):
        print("{:d}{:d}".format(number_1, number_2), end=", " if number_1 < 8 else "\n" )
