#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == '+':
        print(f"{a} {op} {b} = {add(a, b)}")
    elif op == '-':
        print(f"{a} {op} {b} = {sub(a, b)}")
    elif op == '*':
        print(f"{a} {op} {b} = {mul(a, b)}")
    elif op == '/':
        print(f"{a} {op} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)