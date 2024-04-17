#!/usr/bin/python3
""" Write a function that reads a text file (UTF8) """

def read_file(filename=""):
    """
    Read the content of a text file and print it to stdout.

    Args:
        filename (str): The name of the text file to read (default is an empty string
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
