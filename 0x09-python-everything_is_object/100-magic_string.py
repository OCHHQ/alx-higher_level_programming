#!/usr/bin/python3
def magic_string():i
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return "BestSchool" * magic_string.counter
