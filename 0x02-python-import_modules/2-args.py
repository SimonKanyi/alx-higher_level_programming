#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("{:d} arguments:".format(len(argv) - 1))
    print(".")
else:
    print("{:d} argument{}:".format(len(argv) - 1, "" if len(argv) == 2 else "s"))
    for i, arg in enumerate(argv[1:], 1):
        print("{:d}: {}".format(i, arg))
