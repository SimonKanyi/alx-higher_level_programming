#!/usr/bin/python3.8
import dis
import sys
import types

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()

    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    names = []
    for name in dir(module):
        if not name.startswith("__"):
            names.append(name)

    names.sort()
    for name in names:
        print(name)