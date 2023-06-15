#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_vals = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    conv_int = 0
    prev_val = 0
    for char in reversed(roman_string):
        val = roman_vals[char]
        if val >= prev_val:
            conv_int += val
        else:
            conv_int -= val
        prev_val = val
    return conv_int
