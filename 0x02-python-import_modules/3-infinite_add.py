#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from the arguments

    total_sum = 0

    for arg in args:
        total_sum += int(arg)

    print(total_sum)