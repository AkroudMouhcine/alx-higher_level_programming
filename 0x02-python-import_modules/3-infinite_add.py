#!/usr/bin/python3
import sys


def add_arguments(arguments):
    total = sum(int(arg) for arg in arguments)
    print(total)


if __name__ == "__main__":
    add_arguments(sys.argv[1:])
