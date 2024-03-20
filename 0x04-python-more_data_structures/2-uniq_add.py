#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    for integer in my_list:
        unique_integers.add(integer)
    sum_unique_integers = sum(unique_integers)
    return sum_unique_integers
