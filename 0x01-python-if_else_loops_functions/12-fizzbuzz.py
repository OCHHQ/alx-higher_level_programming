#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print("FIZZ ", end='')
        elif i % 5 == 0 and i % 3 != 0:
            print("BUZZ ", end='')
        elif i % 5 == 0 and i % 3 == 0:
            print("FIZZBUZZ ", end='')
        else:
            print("{} ".format(i), end='')
