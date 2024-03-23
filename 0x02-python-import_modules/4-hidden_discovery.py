#!/usr/bin/python3
import dis
import sys

if __name__ == "__main__":
    sys.path.append(".")
    from hidden_4 import *

    names = dir()
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)