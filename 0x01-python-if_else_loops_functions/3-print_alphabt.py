#!/usr/bin/python3
for number in range(97, (97 + 26)):
    if number == 101 or number == 113:
        continue
    else:
        print("{number:c}".format(number=number), end="")
