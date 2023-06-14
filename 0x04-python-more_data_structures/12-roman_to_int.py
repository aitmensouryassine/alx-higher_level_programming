#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    numerals = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    numerals_keys = list(enumerate(numerals))
    prev = ""
    sum = 0
    for letter in roman_string:
        for i, k in numerals_keys:
            if letter == k:
                sub = 1 if letter == "V" else 2
                if prev == numerals_keys[i - sub][1]:
                    sum += numerals[k] - \
                        (numerals[numerals_keys[i - sub][1]] * 2)
                else:
                    sum += numerals[k]
                    prev = k

    return sum
