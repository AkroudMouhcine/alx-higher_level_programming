#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_ints = set()
    for num in my_list:
        unique_ints.add(num)
    sum_of_unique = sum(unique_ints)
    return sum_of_unique
