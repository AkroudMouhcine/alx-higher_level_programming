#!/usr/bin/python3
def uppercase(str_):
    for char in str_:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            tmp = chr(ord(char) - 32)
        else:
            tmp = char
        print("{}".format(tmp), end="")
    print("")
