#!/usr/bin/python3
import sys


def count_arguments(args):
    num_args = len(args)
    return num_args


def print_arguments(args):
    for index, arg in enumerate(args):
        print(f"{index}: {arg}")


if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = count_arguments(args)
    print(f"{num_args} argument{'s' if num_args != 1 else ''}\
{'.' if num_args == 0 else ':'}")
    print_arguments(args)
