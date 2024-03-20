#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    print("{} + {} = {}".format(a, b, addition_result))
    print("{} - {} = {}".format(a, b, subtraction_result))
    print("{} * {} = {}".format(a, b, multiplication_result))
    print("{} / {} = {}".format(a, b, division_result))