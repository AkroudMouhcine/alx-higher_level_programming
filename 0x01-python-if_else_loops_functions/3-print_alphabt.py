#!/usr/bin/python3
for the_alphabet in range(ord('a'), ord('z')+1):
    if chr(the_alphabet) not in ['q', 'e']:
        print(chr(the_alphabet), end='')
